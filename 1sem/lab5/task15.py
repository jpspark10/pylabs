import sys
from functools import reduce


def main():
    lines = [line.strip() for line in sys.stdin]

    min_value = reduce(lambda x, y: x if x < y else y, lines)

    print(min_value)


if __name__ == "__main__":
    main()
