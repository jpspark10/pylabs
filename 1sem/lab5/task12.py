def sort_points(points):
    def distance(point):
        return point[0] ** 2 + point[1] ** 2

    sorted_points = sorted(points, key=lambda p: (distance(p), p[0], p[1]))
    return sorted_points


def main():
    points = [(1, 2), (2, 1), (1, -1), (-1, -1), (0, 0)]
    sorted_points = sort_points(points)

    for point in sorted_points:
        print(point)


if __name__ == "__main__":
    main()
