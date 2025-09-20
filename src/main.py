from src.utils import read_json_file
from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.load_files import load_csv_file, load_excel_file
from src.generators import filter_by_currency
from src.widget import get_date, mask_account_card


if __name__ == "__main__":

    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    question_text = """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """

    print(question_text)
    type_source = input('Пользователь: ')

    while type_source not in ["1", "2", "3"]:

        print('Программа: Вы указали не верный вариант')
        print(question_text)
        type_source = input('Пользователь: ')

    if type_source == "1":
        print("Программа: Для обработки выбран JSON - файл.")
        data = read_json_file('../data/operations.json')
        type_source = 'json'
    elif type_source == "2":
        print("Программа: Для обработки выбран CSV - файл.")
        data = load_csv_file('../data/transactions.csv')
        type_source = 'csv'
    elif type_source == "3":
        print("Программа: Для обработки выбран EXCEL - файл.")
        data = load_excel_file('../data/transactions_excel.xlsx')
        type_source = 'excel'

    question_text = """Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""

    print(question_text)
    status = input('Пользователь: ')

    while status.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:

        print(f'Программа: Статус операции "{status}" недоступен.')
        print(question_text)
        status = input('Пользователь: ')

    print(f'Программа: Операции отфильтрованы по статусу "{status}"')

    filter_data = filter_by_state(data, status.upper())

    #Сортировка операций по дате

    question_text = "Программа: Отсортировать операции по дате? Да / Нет"
    print(question_text)
    date_sort = input('Ввод: ')

    while date_sort.upper() not in ["ДА", "НЕТ"]:
        print(f'Программа: Введен некорректный ответ {date_sort}.')
        print(question_text)
        date_sort = input('Пользователь: ')

    sort_reverse = True
    if date_sort.upper() == "ДА":
        question_text = "Программа: Отсортировать по возрастанию или по убыванию?"
        print(question_text)
        type_sort_reverse = input('Ввод: ')

        while type_sort_reverse.lower() not in ["по возрастанию", "по убыванию"]:
            print(f'Программа: Введен некорректный ответ {type_sort_reverse}.')
            print(question_text)
            type_sort_reverse = input('Пользователь: ')

        sort_reverse = type_sort_reverse.lower() == "по возрастанию"

        filter_data = sort_by_date(filter_data, sort_reverse=sort_reverse)

    # Выводить только рублевые транзакции?

    question_text = "Программа: Выводить только рублевые транзакции? Да / Нет"
    print(question_text)
    filter_currency = input('Ввод: ')

    while filter_currency.upper() not in ["ДА", "НЕТ"]:
        print(f'Программа: Введен некорректный ответ {filter_currency}.')
        print(question_text)
        filter_currency = input('Пользователь: ')

    currency_code = ""
    if filter_currency.upper() == "ДА":
        currency_code = "RUB"


    # Отфильтровать список транзакций по определенному слову в описании
    question_text = "Программа: Отфильтровать список транзакций по определенному слову в описании? Да / Нет"
    print(question_text)
    filter_by_word = input('Ввод: ')

    while filter_currency.upper() not in ["ДА", "НЕТ"]:
        print(f'Программа: Введен некорректный ответ {filter_by_word}.')
        print(question_text)
        filter_by_word = input('Пользователь: ')

    if filter_by_word.upper() == "ДА":
        print(f'Программа: Введите слово для фильтра.')
        filter_word = input('Пользователь: ')
        filter_data = process_bank_search(filter_data, filter_word)

    if currency_code == "RUB":
        filter_data = list(filter_by_currency(filter_data, currency_code, type_source))

    count_transactions = len(filter_data)

    if count_transactions > 0:
        print('Программа: Распечатываю итоговый список транзакций...')
        print(f'Программа: Всего банковских операций в выборке: {len(filter_data)}')

        for item in filter_data:
            print(f'id {item['id']}')
            date_transaction = item.get('date', '')
            if date_transaction != '':
                print(f'{get_date(date_transaction)} {item.get('description','')}')
            else:
                print(f'{item.get('description', '')}')
            account_card_from = item.get('from', '')
            account_card_to = item.get('to', '')
            if account_card_from != '' and account_card_to != '':
                print(f'{mask_account_card(account_card_from)} -> {mask_account_card(account_card_to)}')
            elif account_card_from != '':
                print(f'{mask_account_card(account_card_from)}')
            elif account_card_to != '':
                print(f'{mask_account_card(account_card_to)}')
            if type_source == "json":
                if item.get('operationAmount', '') != '':
                    amount = item['operationAmount']['amount']
                    currency_code = item['operationAmount']['currency']['code']
                else:
                    amount = ''
                    currency_code = ''
            else:
                amount = item.get('amount', '')
                currency_code = item.get('currency_code', '')
            if amount != '':
                print(f'Сумма: {amount} currency_code')

    else:
        print('Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
