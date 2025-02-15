def first(my_list):
    return [x for x in my_list if x < 5]


def second(my_list):
    return [x / 2 for x in my_list]


def third(my_list):
    return [x * 2 for x in my_list if x > 17]


def fourth():
    return [x ** 2 for x in range(int(input()))]


def fifth():
    numbers = input().split()
    n_list = [int(x) ** 2 for x in numbers]
    print(" ".join(map(str, n_list)))


def sixth():
    return " ".join([str(int(x) ** 2) for x in input().split()
                     if int(x) % 2 != 0 and (int(x) ** 2) % 10 != 9])


if __name__ == "__main__":
    print(first([1, 2, 3, 4, 5, 6, 76]))
    print(second([1, 2, 3, 4, 5, 6, 76]))
    print(third([1, 2, 3, 4, 5, 6, 76]))
    print(fourth())
    fifth()
    print(sixth())
