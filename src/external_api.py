import requests
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_exchange_rates(currency_from: str, amount: float) -> tuple[bool, dict]:
    """обращение к Exchange Rates Data API для получения тек курса валют и конвертации суммы операции в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_from}&amount={amount}"

    payload = {}
    headers = {
        "apikey": API_KEY
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code != 200:
        return False, 0
    else:
        return True, response.json()['result']
