def square_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a ** 2
        a, b = b, a + b


def main():
    n = 5
    print(f"Квадраты чисел Фибоначчи до {n}:")
    for sf in square_fibonacci(n):
        print(sf)


if __name__ == "__main__":
    main()
