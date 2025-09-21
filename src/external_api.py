import requests
# from dotenv import load_dotenv
import os


# load_dotenv()
# API_KEY = os.getenv('API_KEY')
API_KEY = "XtYJATtPb8t7I7WL5o5o4TtF3mr6rFmw11"


def get_exchange_rates(currency_from: str, amount: float) -> float:
    """обращение к Exchange Rates Data API для получения тек курса валют и конвертации суммы операции в рубли"""
    return 100
    # url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_from}&amount={amount}"
    #
    # payload = {}
    # headers = {
    #     "apikey": API_KEY
    # }
    # response = requests.get(url, headers=headers, data=payload)
    #
    # return response.json()['result']
