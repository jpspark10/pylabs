def third_task():
    numbers1 = list(map(int, input.split()))
    numbers2 = list(map(int, input.split()))
    return set(set(numbers1) & set(numbers2))


if __name__ == "__main__":
    third_task()