from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_card: str) -> str:
    """Обработка информации о картах и о счетах и возвращение замаскированного номеров"""
    name, number = number_card.rsplit(" ", maxsplit=1)
    if name.lower() == "счет":
        mask_number = get_mask_account(number)
    else:
        mask_number = get_mask_card_number(number)
    return f"{name} {mask_number}"


def get_date(date_string: str) -> str:
    """преобразование даты в формат 'ДД.ММ.ГГГГ'"""
    date_string_to_date = datetime.strptime(date_string[0:10], "%Y-%m-%d").date()
    formatted_date = date_string_to_date.strftime("%d.%m.%Y")
    return str(formatted_date)
