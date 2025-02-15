seen = set()


def print_without_duplicates(message):
    if message not in seen:
        seen.add(message)
        print(message)


if __name__ == "__main__":
    print_without_duplicates("Привет")
    print_without_duplicates("Не могу до тебя дозвониться")
    print_without_duplicates("Не могу до тебя дозвониться")
    print_without_duplicates("Не могу до тебя дозвониться")
    print_without_duplicates("Когда доедешь до дома")
    print_without_duplicates("Ага, жду")
    print_without_duplicates("Ага, жду")
