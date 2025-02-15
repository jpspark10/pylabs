def main():
    input_string = input("Введите строку: ")

    words = input_string.split()

    sorted_words = sorted(words, key=lambda x: x.lower())

    print(" ".join(sorted_words))


if __name__ == "__main__":
    main()
