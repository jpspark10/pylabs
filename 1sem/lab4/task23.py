def matrix(n=1, m=None, a=0):
    if m is None:
        m = n
    return [[a] * m for _ in range(n)]


if __name__ == "__main__":
    rows = matrix()
    for row in rows:
        print(*row)

    rows = matrix(2)
    for row in rows:
        print(*row)

    rows = matrix(2, 3)
    for row in rows:
        print(*row)
