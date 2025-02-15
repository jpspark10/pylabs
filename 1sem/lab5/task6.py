def arithmetic_operation(operation):
    if operation == '+':
        return lambda x, y: x + y
    elif operation == '-':
        return lambda x, y: x - y
    elif operation == '*':
        return lambda x, y: x * y
    elif operation == '/':
        return lambda x, y: x / y
    else:
        raise ValueError("Неподдерживаемая операция")


if __name__ == "__main__":
    operation = arithmetic_operation('+')
    print(operation(1, 5))
