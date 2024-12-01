class Point:
    def __init__(self, x, y):
        pass


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(5, 6)

    if p1 == p2:
        print("Equal True")
    else:
        print("Equal False")

    if p1 != p2:
        print("Not equal True")
    else:
        print("Not equal False")
