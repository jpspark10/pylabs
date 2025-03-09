from logger import logger


def load_dictionary(file_name):
    logger.info(f"Загрузка словаря из файла: {file_name}")
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            dictionary = set(f.read().splitlines())
            logger.info(f"Словарь загружен, найдено {len(dictionary)} слов")
            return dictionary
    except Exception as e:
        logger.error(f"Ошибка при загрузке словаря: {str(e)}")
        raise e
