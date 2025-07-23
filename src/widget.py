from masks import get_mask_card_number, get_mask_account


def mask_account_card(number_card: str) -> str:
    """Обработка информации о картах и о счетах и возвращение замаскированного номерв"""
    words = number_card.split()
    if "счет" in number_card.lower():
        return number_card.replace(words[-1],'') + get_mask_account(words[-1])
    else:
        return number_card.replace(words[-1],'') + get_mask_card_number(words[-1])


with open(r'tests/test_data.txt', 'r', encoding='utf-8') as file_test:
    for line_file in file_test:
        print(mask_account_card(line_file))