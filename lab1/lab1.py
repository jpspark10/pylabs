def first_task():
    film_name = input()
    cinema_name = input()
    time = input()

    msg = f'Билет на "{film_name}" в "{cinema_name}" на {time} забронирован.'
    print(msg)


def second_task():
    first_word = input()
    second_word = input()

    def check_word(word, word2):
        return (word == 'да' and word2 == 'да') or (word == 'нет' and word2 == 'нет')

    if check_word(first_word, second_word):
        print("ВЕРНО")
    else:
        print('НЕВЕРНО')


def third_task():
    login = input()
    reserve = input()
    return '@' not in login and '@' in reserve


def fourth_task():
    print(input())


def fifth_task():
    user_input = input()

    if user_input == '':
        print('Да')
    else:
        print('Нет')


def sixth_task():
    number = int(input())
    midnumb = number % 100 % 10 + number % 100 // 10 + number // 100 - (max(number % 100 % 10,number % 100 // 10,number // 100) + min(number % 100 % 10,number % 100 // 10,number // 100))
    if (max(number % 100 % 10,number % 100 // 10,number // 100) + min(number % 100 % 10,number % 100 // 10,number // 100))/2 == midnumb:
        print('Вы ввели красивое число.')
    else:
        print('Жаль, вы ввели обычное число.')


def seventh_task():
    num = int(input())
    a = num % 10
    num //= 10
    b = num % 10
    num //= 10
    c = num % 10
    d = num // 10
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if c > d:
        c, d = d, c
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    if a == 0 and b:
        a, b = b, a
    elif a == 0 and c:
        a, c = c, a
    elif a == 0 and d:
        a, d = d, a
    print(d + 10 * (c + 10 * (b + 10 * a)))


def eighth_task():
    user_input = input()
    max_height = 0
    min_height = int(user_input) + 1
    count = 0
    while user_input != '!':
        user_input = int(user_input)
        if 150 <= user_input <= 190:
            count += 1
            if user_input > max_height:
                max_height = user_input
            elif user_input < min_height:
                min_height = user_input
        user_input = input()
    if count == 0:
        print('нету космонавтов :( ')
    else:
        print(str(count) + '\n' + f'{min_height} {max_height}')


def nineth_task():
    while True:
        password1 = input()
        password2 = input()
        if len(password1) < 8:
            print("Короткий!")
            continue
        if "123" in password1:
            print("Простой!")
            continue
        if password1 != password2:
            print("Различаются.")
            continue

        print("OK")
        break


def eleventh_task():
    height = int(input())
    for i in range(height):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)


def twelth_task():
    number = int(input())
    line = 1
    i = 1
    while i <= number:
        for j in range (line):
            print (f'{i} ', end = '')
            i += 1
            if i > number:
                break
        print('\n', end = '')
        line += 1


def thirteenth_task():
    length = int(input())
    height = int(input())
    symb = input()
    for i in range (height):
        if i == 0 or i == height - 1:
            print (symb * length)
        else:
            print(symb + str(' ' * (length - 2)) + symb)


def tenth_task():
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    results = []

    while True:
        first_num = int(input('Введите первое число: '))
        operation = input('Введите операцию: ')

        if operation == 'x':
            break

        second_num = None
        if operation in ['+', '-', '*', '/', '%']:
            try:
                second_num = int(input('Введите второе число: '))
            except ValueError as e:
                print('Некорректный ввод второго числа')
                continue

        if operation == '!':
            results.append(factorial(first_num))
        elif operation in ['+', '-', '*', '/', '%']:
            if operation == '+':
                results.append(first_num + second_num)
            elif operation == '-':
                results.append(first_num - second_num)
            elif operation == '*':
                results.append(first_num * second_num)
            elif operation == '/':
                results.append(first_num // second_num)
            else:
                results.append(first_num % second_num)

    for result in results:
        print(result)
