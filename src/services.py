import pandas as pd
import calendar
import math
import logging
import json

from src.logger import setup_logging
from datetime import datetime, timedelta
from typing import Any


name_logger = __name__
logger = setup_logging(name_logger)
file_handler = logging.FileHandler('log/utils.log')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def investment_bank(month: str, transactions: list[dict[str,Any]], limit: int) -> json:
    """округляет расходы в списке транзакций до шага округления limit, и возвращает
    разницу между фактической суммой трат по карте и суммой округления, которая будет
    попадать насчет «Инвесткопилки»"""
    try:
        date_start = datetime.strptime(f'{month}-01', '%Y-%m-%d')
    except ValueError:
        logger.error(f"Неверный формат даты и времени для параметра month. Используйте YYYY-MM")
        raise ValueError("Неверный формат даты и времени для параметра month. Используйте YYYY-MM")

    df = pd.DataFrame(transactions)
    df['Дата операции'] = pd.to_datetime(df['Дата операции'], format='%d.%m.%Y %H:%M:%S', errors='coerce')

    number_of_days = calendar.monthrange(int(month[0:4]), int(month[5:]))[1]
    date_end = date_start + timedelta(days=number_of_days)

    df_month = df.loc[(df['Дата операции'] >= date_start)
                   & (df['Дата операции'] < date_end)][['Сумма операции','Дата операции','Валюта операции']]
    df_month['payment_amount_module'] = df_month['Сумма операции'].abs()
    df_month['investment_amount'] = ((df_month['payment_amount_module'].apply(math.ceil) + (
                limit - 1)) // limit * limit) - df_month['payment_amount_module']
    sum_investment = round(df_month['investment_amount'].sum(),2)

    result = json.dumps({"investment_amount" : float(sum_investment)})
    return result
