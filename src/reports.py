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
    df_copy = transactions.dropna(subset=['Дата операции']).copy()
    df_filter = df_copy[(df_copy['Дата операции'] >= three_months_ago)
                & (df_copy['Дата операции'] < date_value)
                & (df_copy['Категория'] != 'Переводы')
                & (df_copy['Сумма операции'] < 0)].sort_values(by='Дата операции')[['Дата операции', 'Сумма операции']]
    df_filter['weekday'] = df_filter['Дата операции'].dt.weekday
    df_filter['day_type'] = df_filter['weekday'].apply(lambda x: 'Weekday' if x < 5 else 'Weekend')

    average_spending_by_workday = df_filter.groupby('day_type')['Сумма операции'].mean()
    return average_spending_by_workday