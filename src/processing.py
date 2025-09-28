import re
from typing import Iterable, Optional
from datetime import datetime
from src.decorators import log


@log(filename="mylog.txt")
def filter_by_state(list_to_filter: list[dict], state_to_filter: Optional[str] = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и возвращает список словарей, содержащий только те,
    у которых статус state (по умолчанию 'EXECUTED') соответствует переданному значению"""
    if state_to_filter == "" or state_to_filter is None:
        state_to_filter = "EXECUTED"
    if list_to_filter == [] or list_to_filter is None:
        raise ValueError("Список банковских операций пуст")
    else:
        filtered_list = []
        for item in list_to_filter:
            if state_to_filter == item.get("state",""):
                filtered_list.append(item)

        return filtered_list


@log(filename="mylog.txt")
def sort_by_date(filtered_list: Iterable[dict], sort_reverse: Optional[bool] = True) -> list[dict]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    и возвращает новый список, отсортированный по дате"""
    if filtered_list == [] or filtered_list is None:
        raise ValueError("Список банковских операций пуст")
    elif sort_reverse is None:
        sort_reverse = True

    for item_list in filtered_list:
        try:
            datetime.strptime(item_list["date"][0:10], "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Переданы некорректные или нестандартные форматы дат")

    return sorted(filtered_list, key=lambda item: item["date"], reverse=sort_reverse)


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании есть данная строка"""

    result_list = []

    pattern = re.compile(search.lower())

    for item in data:
        if pattern.match(item["description"].lower()):
            result_list.append(item)

    return result_list


def process_bank_operations(data:list[dict], categories:list)->dict:
    """принимает список словарей с данными о банковских операциях и список категорий операций,
    и возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""

    category_counts = {category: 0 for category in categories}
    for transaction in data:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
                break
    return category_counts
