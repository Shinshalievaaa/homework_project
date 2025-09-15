import pytest
import csv
import pandas as pd
from unittest.mock import Mock

from src.load_files import load_excel_file, load_csv_file


def test_load_csv_file():
    """тестирование функции для считывания финансовых операций из CSV"""
    mock_csv = Mock(return_value=[])
    csv.DictReader = mock_csv
    assert load_csv_file('data/transactions.csv') == []


@pytest.fixture
def transaction_df():
    df = pd.DataFrame({'id': [650703],
                       'state': ['EXECUTED'],
                       'date': ['2023-09-05T11:30:32Z']
                       ,'amount': ['16210'],
                       'currency_name': ['Sol'],
                       'currency_code': ['PEN'],
                       'from': ['Счет 58803664561298323391'],
                       'to': ['Счет 39745660563456619397'],
                       'description': ['Перевод организации']})
    return df

def test_load_excel_file(transaction_df):
    """тестирование функции для считывания финансовых операций из Excel"""
    mock_excel = Mock(return_value=transaction_df)
    pd.read_excel = mock_excel
    assert load_excel_file('data/transactions_excel.xlsx') == transaction_df.to_dict('records')
