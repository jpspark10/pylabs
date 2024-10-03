def fifth_task():
    n = int(input())

    unique_words = set()

    for _ in range(n):
        line = input().split()
        for word in line:
            unique_words.add(word)

    print(len(unique_words))


if __name__ == "__main__":
    fifth_task()
