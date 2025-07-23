from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(number_card: str) -> str:
    """Обработка информации о картах и о счетах и возвращение замаскированного номерв"""
    words = number_card.split()
    if "счет" in number_card.lower():
        return number_card.replace(words[-1],'') + get_mask_account(int(words[-1]))
    else:
        return number_card.replace(words[-1],'') + get_mask_card_number(int(words[-1]))


def get_date(date_string: str) -> str:
    date_string_to_date = datetime.strptime(date_string[0:10], "%Y-%m-%d").date()
    formatted_date = date_string_to_date.strftime("%d.%m.%Y")
    return str(formatted_date)


with open(r'tests/test_data.txt', 'r', encoding='utf-8') as file_test:
    for line_file in file_test:
        print(mask_account_card(line_file))

print(get_date("2024-03-11T02:26:18.671407"))
