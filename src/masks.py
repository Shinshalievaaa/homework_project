import logging
from src.decorators import log
from logger import setup_logging


name_logger = __name__
logger = setup_logging(name_logger)
file_handler = logging.FileHandler('log/masks.log')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


@log(filename="mylog.txt")
def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    logger.info(f"Начало получения маски номера карты {card_number}")
    if card_number == "":
        logger.error(f"Передан пустой номер карты")
        raise ValueError("Передан пустой номер карты")
    elif len(card_number) != 16:
        logger.error(f"Длина номера карты {len(card_number)} не равна 16")
        raise ValueError("Длина номера карты не равна 16")
    elif any(x.isalpha() for x in card_number):
        logger.error(f"Номер карты содержит не числовые данные")
        raise ValueError("Номер карты содержит не числовые данные")
    else:
        mask_card = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        logger.info(f"Получена маска {mask_card}")
        return mask_card


@log(filename="mylog.txt")
def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    logger.info(f"Начало получения маски номера счета {account_number}")
    if account_number == "":
        logger.error(f"Передан пустой номер счета")
        raise ValueError("Передан пустой номер счета")
    elif len(account_number) != 20:
        logger.error(f"Длина номера счета {len(account_number)} не равна 20")
        raise ValueError("Длина номера счета не равна 20")
    elif (x.isalpha() for x in account_number):
        logger.error(f"Номера счета содержит не числовые данные")
        raise ValueError("Номера счета содержит не числовые данные")
    else:
        mask_account = "**" + account_number[-4:]
        logger.info(f"Получена маска {mask_account}")
        return mask_account
