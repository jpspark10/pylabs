from math import sqrt


def distance(x1, x2, y1, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


if __name__ == "__main__":
    print(distance(1, 3, 3, 5))
