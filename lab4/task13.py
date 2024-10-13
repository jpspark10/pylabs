def compare_sort_methods():
    arr = [5, 3, 8, 1, 9]

    arr.sort()
    print("Список после вызова sort():", arr)

    arr2 = [5, 3, 8, 1, 9]

    new_sorted_arr = sorted(arr2)
    print("Исходный список arr2 после вызова sorted():", arr2)
    print("Новый отсортированный список:", new_sorted_arr)


if __name__ == "__main__":
    compare_sort_methods()
