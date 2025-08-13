import pytest
from src.masks import get_mask_card_number


@pytest.mark.parametrize("card_number, mask_card_number", [('7000792289606361', '7000 79** **** 6361'),
                                                           ('8000192289606300', '8000 19** **** 6300'),
                                                           ('9000322289601234', '9000 32** **** 1234')])
def test_get_mask_card_number(card_number, mask_card_number):
    """Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number(card_number) == mask_card_number



###Проверка работы функции на различных входных форматах номеров карт,
# включая граничные случаи и нестандартные длины номеров.###
###Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.###

