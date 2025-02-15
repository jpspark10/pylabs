import sys

if __name__ == "__main__":
    print(any('0' in row for row in [line.split() for line in sys.stdin]))
