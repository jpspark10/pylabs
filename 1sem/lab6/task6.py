class SparseArray:
    def __init__(self):
        self.data = {}

    def __setitem__(self, index, value):
        if value != 0:
            self.data[index] = value
        elif index in self.data:
            del self.data[index]

    def __getitem__(self, index):
        return self.data.get(index, 0)


if __name__ == "__main__":
    arr = SparseArray()
    arr[1] = 10
    arr[8] = 20
    for i in range(10):
        print('arr[{}] = {}'.format(i, arr[i]))
