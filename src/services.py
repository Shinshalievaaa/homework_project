import pandas as pd
import math

from src.utils import (get_transactions_data)


def investment_bank(month: str, transactions: list[dict[str,any]], limit: int) -> float:
    """округляет расходы в списке транзакций до шага округления limit, и возвращает
    разницу между фактической суммой трат по карте и суммой округления, которая будет
    попадать насчет «Инвесткопилки»"""
    df = pd.DataFrame(transactions)
    df_month = df.loc[(df['Дата операции'].str.slice(6, 10) == month[0:4])
                      & (df['Дата операции'].str.slice(3, 5) == month[5:7])][['Сумма операции','Дата операции','Валюта операции']]
    df_month['payment_amount_module'] = df_month['Сумма операции'].abs()
    df_month['investment_amount'] = ((df_month['payment_amount_module'].apply(math.ceil) + (
                limit - 1)) // limit * limit) - df_month['payment_amount_module']
    sum_investment = df_month['investment_amount'].sum()
    return sum_investment


if __name__ == '__main__':
    transactions_data = get_transactions_data()
    print(f'sum_investment: {investment_bank(transactions_data, 50)}')
