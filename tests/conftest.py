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