def check_password(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            input_password = input("Введите пароль: ")
            if input_password == password:
                return func(*args, **kwargs)
            else:
                print("В доступе отказано")
                return None

        return wrapper

    return decorator


@check_password('password')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    print(f"Готовлю бургер с {typeOfMeat}, лук: {withOnion}, томаты: {withTomato}")


if __name__ == "__main__":
    make_burger("говядина", withOnion=True)
