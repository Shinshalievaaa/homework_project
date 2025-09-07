import json
from src.external_api import get_exchange_rates


def read_json_file(path: str) -> dict:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    data = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data
            except json.decoder.JSONDecodeError:
                return data
    except FileNotFoundError:
        return data


def get_transaction_amount(transaction: dict) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = transaction.get("operationAmount", {}).get("amount")
    if amount:
        currency = transaction.get("operationAmount", {}).get('currency')
        if currency['code'] == 'RUB':
            return float(amount)
        else:
            return round(get_exchange_rates(currency['code'], float(amount)), 2)
    else:
        return 0
