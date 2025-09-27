import pandas as pd
from typing import Optional
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
# pip install python - dateutil


def spending_by_workday(transactions: pd.DataFrame, end_date: Optional[str] = None) -> pd.DataFrame:
    """выводит средние траты в рабочий и в выходной день за последние три месяца (от переданной даты)"""
    if end_date is None:
        date_value = datetime.combine(date.today(), datetime.min.time())
    else:
        date_value = datetime.strptime(end_date, '%d.%m.%Y')

    three_months_ago = date_value - relativedelta(months=3)
    date_value = date_value + timedelta(days=1)
    transactions['Дата операции'] = pd.to_datetime(transactions['Дата операции'], errors='coerce')
    df_cleaned = transactions.dropna(subset=['Дата операции']).copy()
    df_new = df_cleaned[(df_cleaned['Дата операции'] >= three_months_ago)
                        & (df_cleaned['Дата операции'] < date_value)
                        & (df_cleaned['Категория'] != 'Переводы')
                        & (df_cleaned['Сумма операции'] < 0)].sort_values(by='Дата операции')[['Дата операции', 'Сумма операции']]
    df_new['weekday'] = df_new['Дата операции'].dt.weekday
    df_new['day_type'] = df_new['weekday'].apply(lambda x: 'Weekday' if x < 5 else 'Weekend')

    average_spending = df_new.groupby('day_type')['Сумма операции'].sum()
    return average_spending