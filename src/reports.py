import pandas as pd
from typing import Optional
import pandas as pd
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

# pip install python - dateutil
from src.utils import (get_transactions_data)


def spending_by_weekday(transactions: pd.DataFrame, date: Optional[str] = None) -> pd.DataFrame:
    if not date:
        date_value = datetime.combine(date.today(), datetime.min.time())
    else:
        date_value = datetime.strptime(date, '%d.%m.%Y')

    three_months_ago = date_value - relativedelta(months=3)
    date_value = date_value + timedelta(days=1)
    # print(date_value)
    # print(three_months_ago)
    df_new = transactions[(transactions['Дата операции'].astype('datetime64[ns]') >= three_months_ago)
                & (transactions['Дата операции'].astype('datetime64[ns]') < date_value)].sort_values(by='Дата операции')[['Дата операции', 'Сумма операции']]
    df_new2 = df_new.groupby('Дата операции')
    mean_price_by_country = df_new2['Сумма операции'].sum()
    # print(mean_price_by_country)