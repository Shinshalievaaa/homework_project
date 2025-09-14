import csv
import pandas as pd

def load_csv_file(path: str) -> list:
    """функция для считывания финансовых операций из CSV"""
    with open('data/transactions.csv', encoding='UTF') as file:
        reader = csv.DictReader(file, delimiter=';')
        return list(reader)


def load_excel_file(path: str) -> list:
    """функция для считывания финансовых операций из Excel"""
    df = pd.read_excel('data/transactions_excel.xlsx')
    # Преобразование в список словарей
    data = df.to_dict('records')
    return data
