from lab6.task17.Conference import Conference


def main():
    print("Добро пожаловать в систему планирования конференций!")
    conference_name = input("Введите название конференции: ")
    conference = Conference(conference_name)

    while True:
        print("\nМеню:")
        print("1. Добавить доклад")
        print("2. Показать расписание")
        print("3. Показать информацию о конференции")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название доклада: ")
            start_time = input("Введите время начала (в формате ЧЧ:ММ): ")
            duration = int(input("Введите длительность доклада (в минутах): "))
            conference.add_talk(title, start_time, duration)
        elif choice == "2":
            conference.display_schedule()
        elif choice == "3":
            print(conference)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
