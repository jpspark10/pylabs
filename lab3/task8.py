def task_eight():
    n = int(input())

    synonyms = {}

    for _ in range(n):
        word1, word2 = input().split()
        synonyms[word1] = word2
        synonyms[word2] = word1

    query_word = input()

    print(synonyms.get(query_word, "Синоним не найден"))


if __name__ == "__main__":
    task_eight()
