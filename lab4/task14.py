numbers = [2, 5, 7, 7, 8, 4, 1, 6]
# odd = even = [] (Неправильно, они указывают на один участок памяти).
# Вследствие этого программа не будет разделять четные и нечетные числа
odd = []
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

