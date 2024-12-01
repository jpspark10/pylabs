class Summator:
    def transform(self, n):
        return n

    def sum(self, n):
        return sum(self.transform(n) for n in range(1, n + 1))


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3


if __name__ == "__main__":
    # Сумма натуральных чисел
    summator = Summator()
    print(summator.sum(5))

    # Сумма квадратов чисел
    square_summator = SquareSummator()
    print(square_summator.sum(5))

    # Сумма кубов чисел
    cube_summator = CubeSummator()
    print(cube_summator.sum(5))
