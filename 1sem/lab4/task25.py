import math


def solve(*coefficients):
    if len(coefficients) == 2:
        a, b = coefficients
        if a == 0:
            return "Нет решений" if b != 0 else "Бесконечное количество решений"
        return [-b / a]

    elif len(coefficients) == 3:
        a, b, c = coefficients
        if a == 0:
            if b == 0:
                return "Нет решений" if c != 0 else "Бесконечное количество решений"
            return [-c / b]

        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return "Нет вещественных решений"
        elif discriminant == 0:
            return [-b / (2 * a)]
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return [root1, root2]


if __name__ == "__main__":
    print(sorted(solve(1, 2, 1)))
    print(sorted(solve(1, -3, 2)))
