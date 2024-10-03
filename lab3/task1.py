def first_task():
    numbers = list(map(int, input.split()))
    return len(set(numbers))


if __name__ == "__main__":
    first_task()
