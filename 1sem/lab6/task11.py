from lab6.task10 import Summator


class PowerSummator(Summator):
    def __init__(self, power):
        self.power = power

    def transform(self, n):
        return n ** self.power


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(power=2)


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(power=3)


if __name__ == "__main__":
    # Сумма чисел в степени 2
    square_summator = SquareSummator()
    print(square_summator.sum(5))

    # Сумма чисел в степени 3
    cube_summator = CubeSummator()
    print(cube_summator.sum(5))

    # Сумма чисел в степени 1.5
    power_summator = PowerSummator(1.5)
    print(power_summator.sum(5))