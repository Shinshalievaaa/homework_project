from src.services import investment_bank


def test_filter_by_state(list_operations):
    """Тестирование функции Инвесткопилка"""
    assert investment_bank('2021.12',list_operations, 100) == 178.94