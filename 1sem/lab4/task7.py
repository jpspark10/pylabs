def task(s):
    if s == s[::-1]:
        return "Палиндром"
    return "Не палиндром"


if __name__ == "__main__":
    print(task("Палиндром"))
    print(task("бээб"))
