from typing import Iterable
from typing import Optional


def filter_by_state(list_to_filter: Iterable[dict], state: Optional[str]) -> list[dict]:
    """Dозвращает список словарей, содержащий только те, у которых ключ state соответствует указанному значению"""

    if state is None:
        state = "EXECUTED"

    filtered_list = []
    for item in list_to_filter:
        if state == item["state"]:
            filtered_list.append(item)

    return filtered_list


def sort_by_date(filtered_list: Iterable[dict], sort_reverse: Optional[bool]) -> list[dict]:
    """возвращаtn новый список, отсортированный по дате"""
    if sort_reverse is None:
        sort_reverse = True
    return sorted(filtered_list, key=lambda item: item["date"], reverse=sort_reverse)
