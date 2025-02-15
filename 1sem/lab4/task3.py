def triangle(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        print("Это треугольник")
    else:
        print("Это не треугольник")


if __name__ == "__main__":
    triangle(1, 1, 2)
    triangle(7, 6, 10)
    triangle(20, 13, 17)
