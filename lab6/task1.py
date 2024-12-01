class BigBell:
    def __init__(self):
        self.state = True

    def sound(self):
        if self.state:
            print("ding")
        else:
            print("dong")
        self.state = not self.state


if __name__ == "__main__":
    bell = BigBell()
    for _ in range(5):
        bell.sound()
