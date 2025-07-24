def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    return "**" + account_number[-4:]
