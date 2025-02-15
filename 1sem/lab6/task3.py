class Selector:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_odds(self):
        return [num for num in self.numbers if num % 2 != 0]

    def get_evens(self):
        return [num for num in self.numbers if num % 2 == 0]


if __name__ == "__main__":
    values = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]
    selector = Selector(values)
    odds = selector.get_odds()
    evens = selector.get_evens()
    print(' '.join(map(str, odds)))
    print(' '.join(map(str, evens)))