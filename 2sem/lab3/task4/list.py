class DefaultList(list):
    def __init__(self, default_value, *args):
        super().__init__(*args)
        self.default_value = default_value

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default_value


if __name__ == "__main__":
    # Пример 1
    s = DefaultList(5)
    s.extend([4, 10])
    indexes = [1, 124, 1882]
    for i in indexes:
        print(s[i], end=" ")

    print()

    # Пример 2
    s = DefaultList(51)
    s.extend([1, 5, 7])
    indexes = [0, 2, 1000, -1]
    for i in indexes:
        print(s[i], end=" ")
