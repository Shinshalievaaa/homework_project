def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    if card_number == "":
        raise ValueError("Передан пустой номер карты")
    elif len(card_number) != 16:
        raise ValueError("Длина номера карты не равна 16")
    elif any(x.isalpha() for x in card_number):
        raise ValueError("Номера карт содержит не числовые данные")
    else:
        return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    if account_number == "":
        raise ValueError("Передан пустой номер счета")
    elif len(account_number) != 20:
        raise ValueError("Длина номера счета не равна 20")
    elif any(x.isalpha() for x in account_number):
        raise ValueError("Номера счета содержит не числовые данные")
    else:
        return "**" + account_number[-4:]
