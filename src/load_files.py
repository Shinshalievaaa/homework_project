import csv
import pandas as pd

def load_csv_file(path: str) -> list:
    """функция для считывания финансовых операций из CSV"""
    data = []
    try:
        with open(path, encoding='UTF') as file:
            try:
                data = csv.DictReader(file, delimiter=';')
                return list(data)
            except csv.Error:
                return data

    except FileNotFoundError:
        return data


def load_excel_file(path: str) -> list:
    """функция для считывания финансовых операций из Excel"""
    data = []
    try:
        df = pd.read_excel(path)
        data = df.to_dict('records')
        return data
    except FileNotFoundError:
        return data
