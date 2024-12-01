class Balance:
    def __init__(self):
        self.rightweight = 0
        self.leftweight = 0

    def add_right(self, weight):
        self.rightweight += weight

    def add_left(self, weight):
        self.leftweight += weight

    def result(self):
        if self.rightweight > self.leftweight:
            return "R"
        elif self.leftweight > self.rightweight:
            return "L"
        else:
            return "="


if __name__ == "__main__":
    balance = Balance()
    balance.add_right(10)
    balance.add_left(9)
    balance.add_left(2)
    print(balance.result())
