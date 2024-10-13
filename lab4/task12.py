def demonstrate_operations():
    a = 5
    b = 5

    a = a + 2
    print("a после a = a + 2:", a)

    b += 2
    print("b после b += 2:", b)

    list1 = [1, 2, 3]
    list2 = [1, 2, 3]

    list1 = list1 + [4, 5]
    print("list1 после list1 = list1 + [4, 5]:", list1)

    list2 += [4, 5]
    print("list2 после list2 += [4, 5]:", list2)

    print("list1 и list2 ссылаются на один и тот же объект?", list1 is list2)


if __name__ == "__main__":
    demonstrate_operations()
