import json
import logging
import pandas as pd
import requests
import os

from src.external_api import get_exchange_rates
from src.logger import setup_logging
from src.load_files import load_excel_file
from dotenv import load_dotenv


load_dotenv()
RAPID_API_KEY = os.getenv('RAPID_API_KEY')

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
    """возвращает стоимость списка акций из S&P500 из настроек пользователя"""
    try:
        stock_list = read_json_file("src/user_settings.json")["user_stocks"]
    except ValueError:
        logger.error(f"Не удалось прочитать настройки пользователя")
        return []

    url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/quote"
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
    }

    stock_prices = []
    for stock in stock_list:
        querystring = {"ticker": stock, "type": "STOCKS"}
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        current_price = data['body']['primaryData']['bidPrice']
        stock_prices.append({"stock": stock, "price": current_price})

    return stock_prices


def get_list_exchange_rates() -> list:
    """возвращает списка валют с курсами из настроек пользователя"""
    try:
        currencies_list = read_json_file("src/user_settings.json")["user_currencies"]
    except ValueError:
        logger.error(f"Не удалось прочитать настройки пользователя")
        return []

    currencies_rates = []

    for currency in currencies_list:
        exchange_rates = get_exchange_rates(currency, 1)
        currencies_rates.append({ "currency": currency,
                                  "rate": exchange_rates})

    return currencies_rates


def get_transactions_data() -> list:
    """загружает все банковские операции пользователя"""
    return load_excel_file('data/operations.xlsx')


def get_information_for_each_card(transactions_data) -> list:
    """возвращает сводную информацию по каждой карте"""
    df = pd.DataFrame(transactions_data)
    df_new = df[df['Сумма платежа'] < 0].groupby('Номер карты').agg({'Сумма платежа': 'sum'})
    df_new_ = df_new.reset_index()
    df_new_.rename(columns={'Номер карты': 'last_digits', 'Сумма платежа': 'total_spent'}, inplace=True)
    df_new_['cashback'] = round(df_new_['total_spent'] * 0.01, 2)
    return df_new_.to_dict('records')

def get_top_5_transactions_by_payment_amount(transactions_data) -> list:
    """возвращает топ-5 транзакций по сумме платежа"""
    df = pd.DataFrame(transactions_data)
    df_sort = df.loc[:, ['Дата платежа', 'Сумма платежа', 'Категория', 'Описание']]
    df_sort['abs_amount'] = df_sort['Сумма платежа'].abs()
    df_sort = df_sort.sort_values(by='abs_amount', ascending=False)[0:5]
    df_sort.rename(columns = {'Дата платежа': 'date',
                              'Сумма платежа': 'amount',
                              'Категория': 'category',
                              'Описание': 'description'},
                   inplace=True)
    df_sort = df_sort.drop('abs_amount', axis=1)
    return df_sort.to_dict('records')
