import json


def read_json_file(path: str) -> dict:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data
            except json.decoder.JSONDecodeError:
                return {}
    except FileNotFoundError:
        return {}



# print(read_json_file('data/operations.json'))