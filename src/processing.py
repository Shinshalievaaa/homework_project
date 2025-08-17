from typing import Iterable, Optional
from datetime import datetime


def filter_by_state(list_to_filter: Iterable[dict], state_to_filter: Optional[str] = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и возвращает список словарей, содержащий только те,
    у которых статус state (по умолчанию 'EXECUTED') соответствует переданному значению"""
    if state_to_filter == '' or state_to_filter is None:
        state_to_filter = "EXECUTED"
    if list_to_filter == [] or list_to_filter is None:
        raise ValueError("Список банковских операций пуст")
    else:
        filtered_list = []
        for item in list_to_filter:
            if state_to_filter == item["state"]:
                filtered_list.append(item)

        return filtered_list


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
