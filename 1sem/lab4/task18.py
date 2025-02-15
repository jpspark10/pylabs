def from_string_to_list(string, container):
    string = list(map(int, string.split()))
    container[:] = container + string


if __name__ == "__main__":
    a = [1, 2, 3]
    from_string_to_list("1 3 99 52", a)
    print(*a)
