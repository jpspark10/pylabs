import re


def validate_phone_number(phone_number):
    clean_phone_number = re.sub(r'[^\d]', '', phone_number)

    if re.search(r'[^0-9\s\+\(\)-]', phone_number):
        return "неверный формат"

    if phone_number.count('(') != phone_number.count(')'):
        return "неверный формат"

    if '--' in phone_number:
        return "неверный формат"

    try:
        if not (clean_phone_number.startswith('7') or clean_phone_number.startswith('8')):
            raise ValueError("неверный код страны")

        if len(clean_phone_number) != 11:
            raise ValueError("неверное количество цифр")

        if clean_phone_number.startswith('8'):
            clean_phone_number = '7' + clean_phone_number[1:]

        clean_phone_number = '+' + clean_phone_number

        operator_code = int(clean_phone_number[2:5])
        if not (910 <= operator_code <= 919 or 980 <= operator_code <= 989):  # МТС
            if not (920 <= operator_code <= 939):  # МегаФон
                if not (902 <= operator_code <= 906 or 960 <= operator_code <= 969):  # Билайн
                    raise ValueError("не определяется оператор сотовой связи")

        return clean_phone_number

    except ValueError as e:
        return str(e)
