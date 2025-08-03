from typing import Iterable, Optional


def filter_by_state(list_to_filter: Iterable[dict], state_to_filter: Optional[str] = 'EXECUTED') -> list[dict]:
    """Функция принимает список словарей и возвращает список словарей, содержащий только те,
    у которых статус state (по умолчанию 'EXECUTED') соответствует переданному значению"""
    filtered_list = []
    for item in list_to_filter:
        if state_to_filter == item["state"]:
            filtered_list.append(item)

    return filtered_list


def sort_by_date(filtered_list: Iterable[dict], sort_reverse: Optional[bool] = True) -> list[dict]:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    и возвращает новый список, отсортированный по дате"""
    return sorted(filtered_list, key=lambda item: item['date'], reverse=sort_reverse)
