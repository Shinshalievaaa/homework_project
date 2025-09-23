import pandas as pd
import logging
import math

from logger import setup_logging
from datetime import datetime
from src.utils import (get_transactions_data)


name_logger = __name__
logger = setup_logging(name_logger)
file_handler = logging.FileHandler('log/utils.log')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def investment_bank(month: str, transactions: list[dict[str, any]], limit: int) -> float:
    """округляет расходы в списке транзакций до шага округления limit, и возвращает
    разницу между фактической суммой трат по карте и суммой округления, которая будет
    попадать на счет «Инвесткопилки»"""
    transactions_data = get_transactions_data()
    df = pd.DataFrame(transactions_data)
    df_month = df.loc[(df['Дата операции'].str.slice(6, 10) == month[0:4])
                      & (df['Дата операции'].str.slice(3, 5) == month[5:7])][['Сумма операции','Дата операции','Валюта операции']]
    df_month['payment_amount_module'] = df_month['Сумма операции'].abs()
    df_month['investment_amount'] = ((df_month['payment_amount_module'].apply(math.ceil) + (
                limit - 1)) // limit * limit) - df_month['payment_amount_module']
    sum_investment = df_month['investment_amount'].sum()
    return sum_investment

# df['payment_date'] = df['Дата платежа'].astype(str).apply(
#     lambda x: datetime.strptime(x, '%d.%m.%Y').replace(day=1) if x != 'nan' else None)