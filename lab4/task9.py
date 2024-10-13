def print_without_duplicates(message):
    seen = set()
    result = []
    for word in message.split():
        if word not in seen:
            seen.add(word)
            result.append(word)
    print(" ".join(result))


if __name__ == "__main__":
    print_without_duplicates("Привет")
    print_without_duplicates("Привет как как как дела добавляются?")
    print_without_duplicates("А как дела?")
    print_without_duplicates("А как как")
    print_without_duplicates("Так так так так так так так")
