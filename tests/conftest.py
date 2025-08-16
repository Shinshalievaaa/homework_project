import pytest

@pytest.fixture
def incorrect_len_card_number():
    return ["70007922896063611", "07922896063611"]


@pytest.fixture
def is_letter_card_number():
    return ["700079228960636l", "700O792289606361", "700OI92289606361"]


@pytest.fixture
def incorrect_len_account():
    return ["773654108430135874305", "7365418430135874305"]


@pytest.fixture
def is_letter_account():
    return ["7365410B430135874305", "73654l08430135874305", "736541O8430135874305"]


@pytest.fixture
def incorrect_account_card_number():
    return ['Maestro 159683786870', 'MasterCard 77158300734726758', 'Счет 6468647367889477958O',
            'Счетт 35383033474447895560', 'Visa Classic 6831982476737658',
            'Visa Platinum 89909221l3665229', 'Visa Gold 5999414228426353',
            'Счет 736541084301358743055']


@pytest.fixture
def empty_account_card_number():
    return ['Maestro ', 'MasterCard ', 'Счет ', '' ]


@pytest.fixture
def incorrect_date_string():
    return ['2020-13-11T02:26:18.671407', '2024-11-32T02:26:18.671407', '2025--13T02:26:18.671407'
            '2022-02-29T02:26:18.671407', '2025-06-31T02:26:18.671407', '025-06-13T02:26:18.671407',
            '2020-13-T02:26:18.671407', '-13-11T02:26:18.671407','2020-13--11T02:26:18.671407','']