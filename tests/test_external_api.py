import pytest
import requests
import os
from unittest.mock import patch
from dotenv import load_dotenv
from src.external_api import get_exchange_rates


load_dotenv()
API_KEY = os.getenv('API_KEY')

@patch('requests.get')
def test_get_exchange_rates(mock_get):
    """тестирование обращения к Exchange Rates Data API"""
    mock_get.return_value.json.return_value = {'result': 1000}
    assert get_exchange_rates("EUR",100) == 1000
    mock_get.assert_called_once_with(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=100",
                                     headers={"apikey":API_KEY},
                                     data={})
