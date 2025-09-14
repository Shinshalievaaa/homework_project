import os
from unittest.mock import Mock
from src.utils import read_json_file, get_transaction_amount


def test_read_json_file():
    """тестирование функции по приему путь до JSON-файла и возвращение списка словарей"""
    mock_json = Mock(return_value={})
    json.load = mock_json
    assert get_transaction_amount('data/operations.json') == []


def test_get_transaction_amount_rub():
    """тестирование функции по приему на вход транзакции и возврата суммы транзакции в рублях"""
    in_json_file = read_json_file(os.path.abspath('data/operations.json'))
    mock_round = Mock(return_value=1000)
    round = mock_round
    assert get_transaction_amount(in_json_file[1]) == 10000
