import pytest
import json
from src.views import main


def test_incorrect_date_main():
    """тестирование некорректной даты для функции main"""
    with pytest.raises(ValueError) as exc_info:
        main('2025-13-26 20:22:07')
    assert str(exc_info.value) == "Неверный формат даты и времени. Используйте YYYY-MM-DD HH:MM:SS"


def test_empty_date_main():
    """тестирование пустой даты для функции main"""
    assert main('') == json.dumps({"error": "Передана пустая дата"},ensure_ascii=False)


if __name__ == '__main__':
    test_incorrect_date_main()
    test_empty_date_main()