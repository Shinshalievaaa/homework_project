import logging


def setup_logging(name_logger: str):
    logging.basicConfig(level=logging.DEBUG, filemode='w')  # Перезапись файла при каждом запуске
    return logging.getLogger(name_logger)