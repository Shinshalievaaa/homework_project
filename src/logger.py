import logging


def setup_logging(name_logger: str):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filemode='w')  # Перезапись файла при каждом запуске
    return logging.getLogger(name_logger)