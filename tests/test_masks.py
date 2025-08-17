import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, mask_card_number", [('7000792289606361', '7000 79** **** 6361'),
                                                           ('8000192289606300', '8000 19** **** 6300'),
                                                           ('9000322289601234', '9000 32** **** 1234')])
def test_get_mask_card_number(card_number, mask_card_number):
    """Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number(card_number) == mask_card_number


def test_get_mask_incorrect_len_card_number(incorrect_len_card_number):
    """Тестирование обработки номера карты с граничными случаями и нестандартной длиной номеров"""
    for card_number in incorrect_len_card_number:
        with pytest.raises(ValueError) as exc_info:
            get_mask_card_number(card_number)

        assert str(exc_info.value) == "Длина номера карты не равна 16"


def test_get_mask_is_letter_card_number(is_letter_card_number):
    """Тестирование обработки номера карты с нечисловыми символами"""
    for card_number in is_letter_card_number:
        with pytest.raises(ValueError) as exc_info:
            get_mask_card_number(card_number)

        assert str(exc_info.value) == "Номера карт содержит не числовые данные"


def test_get_mask_empty_card_number():
    """Тестирование обработки номера карты, где отсутствует номер карты"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")

    assert str(exc_info.value) == "Передан пустой номер карты"


@pytest.mark.parametrize("account_number, mask_account", [('64686473678894779589', '**9589'),
                                                         ('35383033474447895560', '**5560'),
                                                         ('73654108430135874305', '**4305')])
def test_get_mask_account(account_number, mask_account):
    """Тестирование правильности маскирования номера счета."""
    assert get_mask_account(account_number) == mask_account


def test_incorrect_len_get_mask_account(incorrect_len_account):
    """Тестирование обработки номера счета с граничными случаями и нестандартной длиной номеров"""
    for account_number in incorrect_len_account:
        with pytest.raises(ValueError) as exc_info:
            get_mask_account(account_number)

        assert str(exc_info.value) == "Длина номера счета не равна 20"


def test_is_letter_get_mask_account(is_letter_account):
    """Тестирование обработки номера счета с нечисловыми символами"""
    for account_number in is_letter_account:
        with pytest.raises(ValueError) as exc_info:
            get_mask_account(account_number)

        assert str(exc_info.value) == "Номера счета содержит не числовые данные"


def test_empty_get_mask_account():
    """Тестирование обработки номера счета, где отсутствует номер счета"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")

    assert str(exc_info.value) == "Передан пустой номер счета"
