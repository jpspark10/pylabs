from datetime import timedelta

from lab6.task17.Talk import Talk


class Conference:
    def __init__(self, name):
        self.name = name
        self.talks = []

    def add_talk(self, title, start_time, duration):
        new_talk = Talk(title, start_time, duration)
        for talk in self.talks:
            if new_talk.overlaps(talk):
                print(f"Ошибка: Доклад '{title}' перекрывается с докладом '{talk.title}'.")
                return
        self.talks.append(new_talk)
        self.talks.sort(key=lambda x: x.start_time)
        print(f"Доклад '{title}' успешно добавлен.")

    def total_talk_time(self):
        return sum((talk.duration for talk in self.talks), timedelta())

    def longest_break(self):
        if len(self.talks) < 2:
            return timedelta(0)
        max_break = timedelta(0)
        for i in range(1, len(self.talks)):
            break_time = self.talks[i].start_time - self.talks[i - 1].end_time
            if break_time > max_break:
                max_break = break_time
        return max_break

    def display_schedule(self):
        print(f"Расписание конференции '{self.name}':")
        for talk in self.talks:
            print(f"  - {talk}")

    def __str__(self):
        total_time = self.total_talk_time()
        max_break = self.longest_break()
        return (
            f"Конференция '{self.name}'\n"
            f"Общее время докладов: {total_time}\n"
            f"Самый длинный перерыв: {max_break}\n"
        )
