import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("filter_list_states, state",
                         [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
                             , 'EXECUTED'),
                          ([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                         'CANCELED')])
def test_filter_by_state(list_states, state, filter_list_states):
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(list_states, state) == filter_list_states


@pytest.mark.parametrize("state", [('EXECUTED'), ('CANCELED'), (''), (None)])
def test_empty_list_filter_by_state(state):
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_state([], state)

    assert str(exc_info.value) == 'Список банковских операций пуст'


@pytest.mark.parametrize("filter_list_states, state",
                         [([]
                             , 'EXEC'),
                          ([]
                             , 'CANCELEDD'),
                          ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
                             , ''),
                          ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
                             , None),
                          ([],
                         'CANC')])
def test_incorrect_state_filter_by_state(list_states, state, filter_list_states):
    """Параметризация тестов для различных возможных значений статуса state"""
    assert filter_by_state(list_states, state) == filter_list_states
