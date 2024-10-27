def sort_by_absolute_value_desc(numbers):
    sorted_numbers = sorted(numbers, key=abs, reverse=True)
    return sorted_numbers


def main():
    numbers = list(map(int, input().split()))
    sorted_numbers = sort_by_absolute_value_desc(numbers)

    print(" ".join(map(str, sorted_numbers)))


if __name__ == "__main__":
    main()
