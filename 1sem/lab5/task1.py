def main():
    numbers = [1, 2, 3, 6, 7, 8, 4, 9, 10, 11, 5, 13, 18, 20]
    result1 = list(filter(lambda x: x < 5, numbers))
    print("Элементы меньше 5:", result1)

    result2 = list(map(lambda x: x / 2, numbers))
    print("Элементы, разделенные на два:", result2)

    result3 = list(map(lambda x: x / 2, filter(lambda x: x > 17, numbers)))
    print("Деление на два элементов больше 17:", result3)

    two_digit_numbers = range(10, 100)
    result4 = sum(map(lambda x: x ** 2, filter(lambda x: x % 9 == 0, two_digit_numbers)))
    print("Сумма квадратов двузначных чисел, делящихся на 9:", result4)


if __name__ == "__main__":
    main()
