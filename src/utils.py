import json
import logging
from src.external_api import get_exchange_rates
from src.logger import setup_logging


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
