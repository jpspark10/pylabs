def check_password(func):
    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")
        if password == "correct_password":
            return func(*args, **kwargs)
        else:
            print("В доступе отказано")
            return None

    return wrapper


@check_password
def secret_function():
    print("Доступ к секретной функции разрешён!")


if __name__ == "__main__":
    secret_function()
