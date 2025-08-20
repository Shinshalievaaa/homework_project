from typing import Iterable


def filter_by_currency(transactions_list, currency_code):
    transactions_filter_list = list(filter(lambda x: x['operationAmount']['currency']['code'] == currency_code, transactions_list))
    for transaction in transactions_filter_list:
        yield transaction


def transaction_descriptions(transactions_list):
    for transaction in transactions_list:
        yield transaction['description']


def card_number_generator(start_num, end_num):
    for i in range(start_num, end_num + 1):
        str_num = str(i)
        num_parts = len(str_num) // 4
        modulo = len(str_num) % 4
        num_parts_zero = 3 - num_parts
        str_end_num = ''
        str_zero = ''
        for x in range(num_parts_zero):
            str_zero += '0000 '
        for y in range(num_parts + 1):
            if modulo > 0 and y == num_parts:
                str_end_num = ' ' + (4 - modulo) * '0' + str_num[0:modulo] + str_end_num
            elif y == 0:
                str_end_num = ' ' + str_num[-1 * y - 4:] + str_end_num
            else:
                str_end_num = ' ' + str_num[-4 * (y + 1):-4 * y] + str_end_num
        yield str(str_zero[0:len(str_zero)-1] + str_end_num).strip()
