def task_seven():
    words = input().split()

    word_count = {}

    for word in words:
        if word in word_count:
            print(word_count[word], end=" ")
            word_count[word] += 1
        else:
            print(0, end=" ")
            word_count[word] = 1


if __name__ == "__main__":
    task_seven()
