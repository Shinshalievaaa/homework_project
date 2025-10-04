import pytest
import json
from src.views import main


@pytest.mark.parametrize("current_date", ["2025-13-26 20:22:07",
                                          "2024-12-01 28:01:05",
                                          "2001-00-01 15:59:43"])
def test_incorrect_date_main(current_date):
    """тестирование некорректной даты для функции main"""
    with pytest.raises(ValueError) as exc_info:
        main(current_date)
    assert str(exc_info.value) == "Неверный формат даты и времени. Используйте YYYY-MM-DD HH:MM:SS"


def test_empty_date_main():
    """тестирование пустой даты для функции main"""
    assert main('') == json.dumps({"error": "Передана пустая дата"},ensure_ascii=False)


if __name__ == '__main__':
    test_incorrect_date_main()
    test_empty_date_main()