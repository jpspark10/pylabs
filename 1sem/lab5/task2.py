def factorials(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact


def main():
    n = 5
    print(f"Факториалы до {n}:")
    for f in factorials(n):
        print(f)


if __name__ == "__main__":
    main()
