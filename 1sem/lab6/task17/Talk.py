from datetime import timedelta, datetime


class Talk:
    def __init__(self, title, start_time, duration):
        self.title = title
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.duration = timedelta(minutes=duration)
        self.end_time = self.start_time + self.duration

    def overlaps(self, other_talk):
        return self.start_time < other_talk.end_time and self.end_time > other_talk.start_time

    def __str__(self):
        start = self.start_time.strftime("%H:%M")
        end = self.end_time.strftime("%H:%M")
        return f"'{self.title}' с {start} до {end}"
    