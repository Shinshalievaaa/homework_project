import json
import logging
import pandas as pd
import requests
from external_api import get_exchange_rates
from logger import setup_logging
from load_files import load_excel_file
# from dotenv import load_dotenv
import os


# load_dotenv()
# API_KEY = os.getenv('RAPID_API_KEY')

name_logger = __name__
logger = setup_logging(name_logger)
file_handler = logging.FileHandler('log/utils.log')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json_file(path: str) -> list:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    data = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                logger.info(f"Получен список словарей из {path}")
                return data
            except json.decoder.JSONDecodeError:
                logger.error(f"Не удалось прочитать файл {path}")
                return data
    except FileNotFoundError:
        return data


def get_transaction_amount(transaction: dict) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    logger.info(f"Попытка прочитать транзакцию")
    amount = transaction.get("operationAmount", {}).get("amount")
    if amount:
        currency = transaction.get("operationAmount", {}).get('currency')
        logger.info(f"Транзакция прочитана")
        if currency['code'] == 'RUB':
            return float(amount)
        else:
            logger.info(f"Получение курса рубля к {currency['code']}")
            return round(get_exchange_rates(currency['code'], float(amount)), 2)
    else:
        logger.warning(f"Не удалось прочитать транзакцию")
        return 0


def get_stock_price() -> list:

    return [{'stock': 'AAPL', 'price': 240.0},
            {'stock': 'AMZN', 'price': 220.82},
            {'stock': 'GOOGL', 'price': 240.73},
            {'stock': 'MSFT', 'price': 485.11},
            {'stock': 'TSLA', 'price': 400.71}]
    # stock_list = read_json_file("src/user_settings.json")["user_stocks"]
    #
    # url = "https://yh-finance8.p.rapidapi.com/stock/get_summary"
    # headers = {
    #     "X-RapidAPI-Key": RAPID_API_KEY
    #     "X-RapidAPI-Host": "yh-finance8.p.rapidapi.com"
    # }
    #
    # stock_prices = []
    # for stock in stock_list:
    #     querystring = {"symbol": stock, "region": "US"}
    #     response = requests.get(url, headers=headers, params=querystring)
    #     data = response.json()
    #     current_price = data[stock]['bid']
    #     stock_prices.append({"stock": stock, "price": current_price})
    #     # print(f"Текущая цена акций Google: {current_price}")
    #
    # return stock_prices


def get_list_exchange_rates() -> list:

    currencies_list = read_json_file("src/user_settings.json")["user_currencies"]

    currencies_rates = []

    for currency in currencies_list:
        currencies_rates.append({ "currency": currency,
                                  "rate": get_exchange_rates(currency,1)})

    return currencies_rates


def get_transactions_data() -> list:
    """"""
    return load_excel_file('data/operations.xlsx')


def get_information_for_each_card(transactions_data) -> list:
    """"""
    df = pd.DataFrame(transactions_data)
    df_new = df[df['Сумма платежа'] < 0].groupby('Номер карты').agg({'Сумма платежа': 'sum'})
    df_new_ = df_new.reset_index()
    df_new_.rename(columns={'Номер карты': 'last_digits', 'Сумма платежа': 'total_spent'}, inplace=True)
    df_new_['cashback'] = round(df_new_['total_spent'] * 0.01, 2)
    return df_new_.to_dict('records')

def get_top_5_transactions_by_payment_amount(transactions_data) -> list:
    """"""
    df = pd.DataFrame(transactions_data)
    df_sort = df.loc[:, ['Дата платежа', 'Сумма платежа', 'Категория', 'Описание']]
    df_sort['Модуль cуммы платежа'] = df_sort['Сумма платежа'].abs()
    df_sort = df_sort.sort_values(by='Модуль cуммы платежа', ascending=False)[0:5]
    df_sort.rename(columns = {'Дата платежа': 'date',
                              'Сумма платежа': 'amount',
                              'Категория': 'category',
                              'Описание': 'description'},
                   inplace=True)
    df_sort = df_sort.drop('Модуль cуммы платежа', axis=1)
    return df_sort.to_dict('records')


print(get_list_exchange_rates())