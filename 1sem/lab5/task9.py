def ask_password(login, password, success, failure):
    vowels = set("aeiouy")

    login_vowels = [char for char in login if char in vowels]
    login_consonants = [char for char in login if char not in vowels]

    password_vowels = [char for char in password if char in vowels]
    password_consonants = [char for char in password if char not in vowels]

    vowel_count_correct = len(password_vowels) == 3
    consonants_correct = login_consonants == password_consonants

    if vowel_count_correct and consonants_correct:
        success(login)
    elif not vowel_count_correct and not consonants_correct:
        failure(login, "Everything is wrong")
    elif not vowel_count_correct:
        failure(login, "Wrong number of vowels")
    else:
        failure(login, "Wrong consonants")


def main(login, password):
    def success(login):
        print(f"Привет, {login}!")

    def failure(login, message):
        print(f"Ктото пытался притвориться пользователем {login}, но в пароле допустил ошибку: {message.upper()}.")

    ask_password(login.lower(), password.lower(), success, failure)


if __name__ == "__main__":
    main("login", "aaalgn")
    main("login", "luagon")
    main("login", "abcd")
