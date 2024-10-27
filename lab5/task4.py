def russian_alphabet():
    for code in range(ord('а'), ord('я') + 1):
        yield chr(code)


def main():
    print("Буквы русского алфавита:")
    for letter in russian_alphabet():
        print(letter, end=' ')
    print()


if __name__ == "__main__":
    main()
