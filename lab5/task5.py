def main():
    russian_alphabet_gen = (chr(code) for code in range(ord('а'), ord('я') + 1))

    print("Буквы русского алфавита:")
    for letter in russian_alphabet_gen:
        print(letter, end=' ')
    print()


if __name__ == "__main__":
    main()
