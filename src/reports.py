import pandas as pd
import logging
import json

from typing import Optional
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


name_logger = __name__
logger = logging.getLogger(name_logger)
file_handler = logging.FileHandler('log/reports.log')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def report_saver(filename=None):
    """записывает в файл результат, который возвращает функция, формирующая отчет"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if filename:
                output_filename = filename
            else:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_filename = f"reports/{func.__name__}_report_{timestamp}.txt"

            try:
                with open(output_filename, 'w', encoding='utf-8') as f:
                    f.write(str(result))
                logger.info(f"Отчет сохранен в файл {output_filename}")
            except IOError as e:
                logger.error(f"Ошибка сохранения отчета в файл {output_filename}: {e}")
                raise ValueError(f"Ошибка сохранения отчета в файл {output_filename}: {e}")
            return result
        return wrapper
    return decorator


@report_saver(None)
def spending_by_workday(transactions: pd.DataFrame, end_date: Optional[str] = None) -> json:
    """выводит средние траты в рабочий и в выходной день за последние три месяца (от переданной даты)"""
    if end_date is None:
        date_value = datetime.combine(date.today(), datetime.min.time())
    else:
        date_value = datetime.strptime(end_date, '%d.%m.%Y')

    three_months_ago = date_value - relativedelta(months=3)
    date_value = date_value + timedelta(days=1)
    transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'], errors='coerce', dayfirst=True)
    df_copy = transactions.dropna(subset=['Дата операции']).copy()
    df_filter = df_copy[(df_copy['Дата операции'] >= three_months_ago)
                & (df_copy['Дата операции'] < date_value)
                & (df_copy['Категория'] != 'Переводы')
                & (df_copy['Сумма операции'] < 0)].sort_values(by='Дата операции')[['Дата операции', 'Сумма операции']]
    df_filter['weekday'] = df_filter['Дата операции'].dt.weekday
    df_filter['day_type'] = df_filter['weekday'].apply(lambda x: 'Weekday' if x < 5 else 'Weekend')

    spending_by_day_type = df_filter.groupby('day_type')['Сумма операции'].mean().round(2)
    return json.dumps({"Weekday": float(spending_by_day_type['Weekday']),
                       "Weekend": float(spending_by_day_type['Weekend'])})
