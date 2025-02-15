def fourth_task():
    numbers = input().split()

    seen = set()

    for num in numbers:
        if num in seen:
            print("YES")
        else:
            print("NO")
            seen.add(num)


if __name__ == "__main__":
    fourth_task()
