class Command:

    def __init__(self, condition, transformation):
        self.condition = condition
        self.transformation = transformation

    def apply(self, numbers):
        return [self.transformation(num) if self.condition(num) else num for num in numbers]


class MakeNegativeCommand(Command):
    def __init__(self):
        super().__init__(condition=lambda x: x > 0, transformation=lambda x: -x)


class SquareCommand(Command):
    def __init__(self):
        super().__init__(condition=lambda x: True, transformation=lambda x: x ** 2)


class StrangeCommand(Command):
    def __init__(self):
        super().__init__(condition=lambda x: x % 5 == 0, transformation=lambda x: x + 1)


def process_numbers(numbers, command_name):
    commands = {
        "make_negative": MakeNegativeCommand(),
        "square": SquareCommand(),
        "strange_command": StrangeCommand(),
    }

    if command_name not in commands:
        raise ValueError(f"Неизвестная команда: {command_name}")

    command = commands[command_name]
    return command.apply(numbers)


if __name__ == "__main__":
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    command_name = input("Введите команду (make_negative, square, strange_command): ").strip()

    try:
        result = process_numbers(numbers, command_name)
        print("Результат:", result)
    except ValueError as e:
        print(e)
