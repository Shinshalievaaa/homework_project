import pytest
from src.widget import mask_account_card, get_date
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


def test_empty_mask_account_card(empty_account_card_number):
    """тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам"""
    for account_card_number in empty_account_card_number:
        with pytest.raises(ValueError):
            get_mask_account(account_card_number)


@pytest.mark.parametrize("date_string, formatted_date", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                                         ("2000-01-31T06:00:13.125258", "31.01.2000"),
                                                         ("2025-08-16T12:41:51.549315", "16.08.2025"),
                                                         ("2020-02-29T23:33:09.124563", "29.02.2020")])
def test_get_date(date_string, formatted_date):
    """Тестирование правильности преобразования даты"""
    assert get_date(date_string) == formatted_date


def test_incorrect_get_date(incorrect_date_string):
    """Проверка работы функции на различных входных форматах даты, включая граничные случаи
    и нестандартные строки и где отсутствует дата"""
    for date_string in incorrect_date_string:
        print(date_string)
        with pytest.raises(ValueError):
            get_date(date_string)
