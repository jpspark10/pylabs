def first_task(inp):
    print(inp[2] + "\n" + inp[-2] + "\n"
          + inp[:5] + "\n" + inp[:-2] + "\n"
          + inp[::2] + "\n" + inp[1::2] + "\n"
          + inp[::-1] + "\n" + inp[-1::-2] + "\n"
          + f'{len(inp)}')


def second_task(inp):
    mid = (len(inp) + 1) // 2
    print(inp[mid:] + inp[:mid])


def third_task(inp):
    print(inp[(inp.rfind('h')):(inp.find('h')):-1])


def fourth_task(inp):
    first_index = inp.find('f')
    if first_index == -1:
        return
    last_index = inp.rfind('f')
    if first_index == last_index:
        print(first_index)
    else:
        print(f"{first_index}\n{last_index}")


def fifth_task():
    first_word = input()
    while True:
        second_word = input()
        if second_word[0] != first_word[-1]:
            print(second_word)
            return
        first_word = second_word


def sixth_task():
    inp = input()
    for i in range(len(inp)):
        print((i + 1) * inp[i], end='')


def seventh_task():
    path = input()

    x = 0
    y = 0
    max_x = 0
    positions = []

    for move in path:
        if move == 'V':
            y += 1
            positions.append((x, y))
        elif move == '<':
            x -= 1
            positions.append((x, y))
        elif move == '>':
            x += 1
            positions.append((x, y))

        max_x = max(max_x, x)

    height = max(y for _, y in positions) + 1

    wall = [[' ' for _ in range(max_x + 1)] for _ in range(height)]

    for x, y in positions:
        wall[y][x] = path[0]

    print(path[0], end='')
    for row in wall:
        print(''.join(row))


def nineth_task(numbers):
    prev = None
    for num in numbers:
        if prev is not None and num > prev:
            print(num)
        prev = num


def tenth_task(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] < 0 and numbers[i + 1] < 0 or numbers[i] > 0 and numbers[i + 1] > 0:
            print(f'{numbers[i]} {numbers[i+1]}')
            break


def eleventh_task(numbers):
    for i in range(0, len(numbers) - 1, 2):
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    print(numbers)


def twelfth_task(numbers):
    unique_elements = []
    seen = set()

    for num in numbers:
        if num not in seen:
            unique_elements.append(num)
            seen.add(num)

    print(unique_elements)


def thirteenth_task():
    word_numbers_str = input()
    original_sentence = input()
    words = original_sentence.split()
    word_numbers = [int(num) for num in word_numbers_str.split()]
    new_sentence_words = [words[num - 1] for num in word_numbers]
    new_sentence = ' '.join(new_sentence_words)
    print(new_sentence.capitalize())


def fifteenth_task():
    class Queue:
        def __init__(self):
            self.queue = []

        def add_to_end(self, patient):
            self.queue.append(patient)

        def add_to_front(self, patient):
            self.queue.insert(0, patient)

        def next_patient(self):
            if not self.queue:
                print("В очереди никого нет.")
            else:
                patient = self.queue.pop(0)
                print(f"Заходит {patient}!")

    # Создаем очередь
    queue = Queue()

    while True:
        command = input()
        if command.startswith("Кто последний?"):
            patient = command.split()[-1]
            queue.add_to_end(patient)
        elif command.startswith("Я только спросить!"):
            patient = command.split()[-1]
            queue.add_to_front(patient)
        elif command == "Следующий!":
            queue.next_patient()
        else:
            print("Неверная команда.")

fifteenth_task()
