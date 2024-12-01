class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(c * (x ** i) for i, c in enumerate(self.coefficients))

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coefficients = [
            (self.coefficients[i] if i < len(self.coefficients) else 0) +
            (other.coefficients[i] if i < len(other.coefficients) else 0)
            for i in range(max_len)
        ]
        return Polynomial(new_coefficients)


if __name__ == "__main__":
    poly1 = Polynomial([0, 0, 1])
    print(poly1(-2))
    print(poly1(-1))
    print(poly1(0))
    print(poly1(1))
    print(poly1(2))
    print()

    poly2 = Polynomial([0, 0, 2])
    print(poly2(-2))
    print(poly2(-1))
    print(poly2(0))
    print(poly2(1))
    print(poly2(2))
    print()

    poly3 = poly1 + poly2
    print(poly3(-2))
    print(poly3(-1))
    print(poly3(0))
    print(poly3(1))
    print(poly3(2))
    print()
