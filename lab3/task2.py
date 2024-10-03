def second_task():
    numbers1 = list(map(int, input.split()))
    numbers2 = list(map(int, input.split()))
    return len(set(numbers1) & set(numbers2))


if __name__ == "__main__":
    second_task()
