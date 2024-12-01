class ReversedList:
    def __init__(self, original_list):
        self.original_list = original_list

    def __len__(self):
        return len(self.original_list)

    def __getitem__(self, index):
        return self.original_list[-(index + 1)]


if __name__ == "__main__":
    rl = ReversedList([10, 20, 30])
    for i in range(len(rl)):
        print(rl[i])
