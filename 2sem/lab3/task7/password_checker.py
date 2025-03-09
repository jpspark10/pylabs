from logger import logger


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class WordError(PasswordError):
    pass


KEYBOARD_SEQUENCES = [
    "qwertyuiop", "asdfghjkl", "zxcvbnm",
    "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю",
    "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM",
    "ЙЦУКЕНГШЩЗХЪ", "ФЫВАПРОЛДЖЭ", "ЯЧСМИТЬБЮ"
]


def check_password(password, dictionary):
    logger.info(f"Начинается проверка пароля: {password}")

    if len(password) < 9:
        logger.error("Пароль слишком короткий")
        raise LengthError("Пароль должен быть не короче 9 символов")

    if not any(c.isdigit() for c in password):
        logger.error("Пароль не содержит цифры")
        raise DigitError("Пароль должен содержать хотя бы одну цифру")

    if not any(c.islower() for c in password) or not any(c.isupper() for c in password):
        logger.error("Пароль не содержит заглавных и строчных букв")
        raise LetterError("Пароль должен содержать хотя бы одну строчную и одну заглавную букву")

    lower_password = password.lower()
    for seq in KEYBOARD_SEQUENCES:
        seq = seq.lower()
        for i in range(len(seq) - 2):
            if seq[i:i + 3] in lower_password:
                logger.error(f"Пароль содержит последовательность: {seq[i:i + 3]}")
                raise SequenceError("Пароль не должен содержать три подряд идущие буквы с клавиатуры")

    if any(word in dictionary for word in password.split()):
        logger.error("Пароль содержит слово из словаря")
        raise WordError("Пароль не должен содержать словарные слова")

    logger.info("Пароль подходит")
    return "Пароль подходит"
