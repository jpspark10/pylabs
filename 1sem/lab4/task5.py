from num2words import num2words


def number_to_word(number):
    return num2words(number, lang='ru')  # Надеюсь так можно, чутка схитрил! =)


if __name__ == "__main__":
    print(number_to_word(123))
    print(number_to_word(1337))
