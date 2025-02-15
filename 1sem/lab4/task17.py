def mirror(arr):
    mirrored_part = arr[::-1]
    arr[:] = arr + mirrored_part


if __name__ == "__main__":
    arr = [1, 2]
    mirror(arr)
    print(arr)
