import json
import logging

from src.logger import setup_logging
from datetime import datetime
from src.utils import (get_stock_price,
                   get_list_exchange_rates,
                   get_transactions_data,
                   get_information_for_each_card,
                   get_top_5_transactions_by_payment_amount)


name_logger = __name__
logger = setup_logging(name_logger)
file_handler = logging.FileHandler('log/utils.log')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def main(current_date: str) -> json:
    """принимает на вход строку с датой и временем в формате YYYY-MM-DD HH:MM:SS
     и возвращает JSON-ответ с данными по всем операциям пользователя, стоимостью акций и курсом валют"""
    if current_date == "":
        return json.dumps({"error": "Передана пустая дата"},ensure_ascii=False)
    else:
        try:
            dt_object = datetime.strptime(current_date, '%Y-%m-%d %H:%M:%S')
            hour = dt_object.hour

            if 5 <= hour < 12:
                greeting = "Доброе утро"
            elif 12 <= hour < 17:
                greeting = "Добрый день"
            elif 17 <= hour < 22:
                greeting = "Добрый вечер"
            else:
                greeting = "Доброй ночи"

            transactions_data = get_transactions_data()
            information_for_cards = get_information_for_each_card(transactions_data)
            top_5_transactions = get_top_5_transactions_by_payment_amount(transactions_data)
            currencies_rates = get_list_exchange_rates()
            stock_prices = get_stock_price()
            response = {"greeting": greeting,
                        "cards": information_for_cards,
                        "top_transactions": top_5_transactions,
                        "currency_rates": currencies_rates,
                        "stock_prices": stock_prices}
            return json.dumps(response)

        except ValueError:
            logger.error(f"Неверный формат даты и времени. Используйте YYYY-MM-DD HH:MM:SS")
            raise ValueError("Неверный формат даты и времени. Используйте YYYY-MM-DD HH:MM:SS")
