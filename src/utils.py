import json
from src.external_api import get_exchange_rates


def read_json_file(path: str) -> dict:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data
            except json.decoder.JSONDecodeError:
                return {}
    except FileNotFoundError:
        return {}


def get_transaction_amount(transaction_json: dict) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if type(transaction_json) is dict:
        values_transaction = transaction_json['operationAmount']
        amount = values_transaction['amount']
        currency = values_transaction['currency']
        currency_code = currency['code']
        if currency_code == 'RUB':
            return amount
        else:
            return round(get_exchange_rates(currency_code, amount), 2)
    else:
        return 0
