def sixth_task():
    n = int(input())
    surname_count = {}

    for _ in range(n):
        surname = input().strip()
        if surname in surname_count:
            surname_count[surname] += 1
        else:
            surname_count[surname] = 1

    same_surname_count = 0
    for count in surname_count.values():
        if count > 1:
            same_surname_count += count

    print(same_surname_count)


if __name__ == "__main__":
    sixth_task()
