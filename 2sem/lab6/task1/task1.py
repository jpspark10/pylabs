import os


def file_size(num_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(num_bytes)
    idx = 0
    while size >= 1024 and idx < len(units) - 1:
        size /= 1024
        idx += 1
    return f"{round(size)}{units[idx]}"


def list_files_sizes():
    for name in os.listdir('.'):
        if os.path.isfile(name):
            size = os.path.getsize(name)
            print(f"{name} {file_size(size)}")


if __name__ == "__main__":
    list_files_sizes()
