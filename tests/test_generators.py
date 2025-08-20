import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize("filter_list_transactions, currency_code",[(
                                                        [{
                                                             "id": 939719570,
                                                             "state": "EXECUTED",
                                                             "date": "2018-06-30T02:08:58.425572",
                                                             "operationAmount": {
                                                                 "amount": "9824.07",
                                                                 "currency": {
                                                                     "name": "USD",
                                                                     "code": "USD"
                                                                 }
                                                             },
                                                             "description": "Перевод организации",
                                                             "from": "Счет 75106830613657916952",
                                                             "to": "Счет 11776614605963066702"
                                                         },
                                                         {
                                                               "id": 142123456,
                                                               "state": "EXECUTED",
                                                               "date": "2019-04-04T23:20:05.206878",
                                                               "operationAmount": {
                                                                   "amount": "79114.93",
                                                                   "currency": {
                                                                       "name": "USD",
                                                                       "code": "USD"
                                                                   }
                                                               },
                                                               "description": "Перевод с карты на карту",
                                                               "from": "Счет 19708645243227123456",
                                                               "to": "Счет 71232167383060284188"
                                                           }],'USD'),
                                                                                                                        ([
                                                         {
                                                                 "id": 112321268,
                                                                 "state": "EXECUTED",
                                                                 "date": "2019-04-04T23:20:05.206878",
                                                                 "operationAmount": {
                                                                     "amount": "598000.93",
                                                                     "currency": {
                                                                         "name": "KZT",
                                                                         "code": "KZT"
                                                                     }
                                                                 },
                                                                 "description": "Перевод с карты на карту",
                                                                 "from": "Счет 29712645248957258542",
                                                                 "to": "Счет 75651555383060284999"
                                                          }],'KZT'),
                                                                                                                        ([
                                                         {
                                                                 "id": 142264268,
                                                                 "state": "EXECUTED",
                                                                 "date": "2019-04-04T23:20:05.206878",
                                                                 "operationAmount": {
                                                                     "amount": "79114.93",
                                                                     "currency": {
                                                                         "name": "RUB",
                                                                         "code": "RUB"
                                                                     }
                                                                 },
                                                                 "description": "Перевод со счета на счет",
                                                                 "from": "Счет 19708645243227258542",
                                                                 "to": "Счет 75651667383060284188"
                                                          }],'RUB')
                                                        ],
                                                        [],'')
def test_filter_by_currency(list_transactions, filter_list_transactions, currency_code):
    currency_transactions = filter_by_currency(list_transactions, currency_code)
    for item in filter_list_transactions:# assert filter_by_currency(list_transactions, currency_code) == filter_list_transactions
        assert next(currency_transactions) == item


@pytest.mark.parametrize("filter_list_transactions, currency_code",[([],'VND')])
def test_filter_no_currency(list_transactions, filter_list_transactions, currency_code):
    currency_transactions = filter_by_currency(list_transactions, currency_code)
    for item in filter_list_transactions:# assert filter_by_currency(list_transactions, currency_code) == filter_list_transactions
        assert next(currency_transactions) == item


@pytest.mark.parametrize("filter_list_transactions, currency_code",[([],'RUB')])
def test_filter_no_list_transactions(filter_list_transactions, currency_code):
    currency_transactions = filter_by_currency([], currency_code)
    for item in filter_list_transactions:# assert filter_by_currency(list_transactions, currency_code) == filter_list_transactions
        assert next(currency_transactions) == item


@pytest.mark.parametrize("list_descriptions",[('Перевод организации',
                                               'Перевод со счета на счет',
                                               'Перевод с карты на карту',
                                               'Перевод организации',
                                               'Перевод с карты на карту')])
def test_transaction_descriptions(list_transactions, list_descriptions):
     descriptions_transactions = transaction_descriptions(list_transactions)
     for item in list_descriptions:  # assert filter_by_currency(list_transactions, currency_code) == filter_list_transactions
         assert next(descriptions_transactions) == item


@pytest.mark.parametrize("list_descriptions",[])
def test_empty_transaction_descriptions(list_transactions, list_descriptions):
     descriptions_transactions = transaction_descriptions([])
     for item in list_descriptions:  # assert filter_by_currency(list_transactions, currency_code) == filter_list_transactions
         assert next(descriptions_transactions) == item


@pytest.mark.parametrize("list_card_number",[('0000 0000 0000 0001',
                                              '0000 0000 0000 0002',
                                              '0000 0000 0000 0003',
                                              '0000 0000 0000 0004',
                                              '0000 0000 0000 0005')])
def test_card_number_generator(list_card_number):
     generator_for_card_number = card_number_generator(1, 5)
     for card_number in list_card_number:  # assert filter_by_currency(list_transactions, currency_code) == filter_list_transactions
          assert next(generator_for_card_number) == card_number


@pytest.mark.parametrize("list_card_number",[('9999 9999 9999 9996',
                                              '9999 9999 9999 9997',
                                              '9999 9999 9999 9998',
                                              '9999 9999 9999 9999')])
def test_border_card_number_generator(list_card_number):
     generator_for_card_number = card_number_generator(9999999999999996, 9999999999999999)
     for card_number in list_card_number:  # assert filter_by_currency(list_transactions, currency_code) == filter_list_transactions
          assert next(generator_for_card_number) == card_number


@pytest.mark.parametrize("list_card_number",[('0000 0001 0007 8912',
                                              '0000 0001 0007 8913',
                                              '0000 0001 0007 8914',
                                              '0000 0001 0007 8915',
                                              '0000 0001 0007 8916')])
def test_middle_card_number_generator(list_card_number):
     generator_for_card_number = card_number_generator(100078912, 100078916)
     for card_number in list_card_number:  # assert filter_by_currency(list_transactions, currency_code) == filter_list_transactions
          assert next(generator_for_card_number) == card_number