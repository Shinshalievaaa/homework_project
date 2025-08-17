def filter_by_currency(transactions_list, currency_code):
    transactions_filter_list = list(filter(lambda x: x['operationAmount']['currency']['code'] == currency_code, transactions_list))
    for transaction in transactions_filter_list:
        yield transaction


def transaction_descriptions(transactions_list):
    for transaction in transactions_list:
        yield transaction['description']