import pytest
from src.widget import mask_account_card
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("account_card_number, mask_account_card_number", [
                                    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                                    ('Счет 64686473678894779589', 'Счет **9589'),
                                    ('Счет 35383033474447895560', 'Счет **5560'),
                                    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                                    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
                                    ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_card(account_card_number, mask_account_card_number):
    """тест, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа
    входных данных (карта или счет)"""
    assert mask_account_card(account_card_number) == mask_account_card_number


def test_incorrect_mask_account_card(incorrect_account_card_number):
    """тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам"""
    for account_card_number in incorrect_account_card_number:
        with pytest.raises(ValueError):
            get_mask_account(account_card_number)
