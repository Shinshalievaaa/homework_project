from typing import Iterable


def filter_by_currency(transactions_list, currency_code) -> Iterable:
    transactions_filter_list = list(filter(lambda x: x['operationAmount']['currency']['code'] == currency_code, transactions_list))
    for transaction in transactions_filter_list:
        yield transaction


def transaction_descriptions(transactions_list) -> Iterable:
    for transaction in transactions_list:
        yield transaction['description']


def card_number_generator(start_num, end_num):
    for i in range(start_num, end_num + 1):
        str_num = str(i)
        k = len(str_num) // 4
        ost = len(str_num) % 4
        n = 3 - k
        str_end_num = ''
        str_zero = ''
        for x in range(n):
            str_zero += '0000 '
        for y in range(k + 1):
            if ost > 0 and y == k:
                str_end_num = ' ' + (4 - ost) * '0' + str_num[0:ost] + str_end_num
            elif y == 0:
                str_end_num = ' ' + str_num[-1 * y - 4:] + str_end_num
            else:
                str_end_num = ' ' + str_num[-4 * (y + 1):-4 * y] + str_end_num
        yield str(str_zero[0:len(str_zero)-1] + str_end_num)

