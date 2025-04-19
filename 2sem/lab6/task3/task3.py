import os
import sys


def human_size(num_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(num_bytes)
    idx = 0
    while size >= 1024 and idx < len(units) - 1:
        size /= 1024
        idx += 1
    return f"{round(size)}{units[idx]}"


def dir_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total


def top10(path):
    items = []
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                sz = dir_size(entry.path)
            else:
                sz = entry.stat().st_size
        except OSError:
            sz = 0
        items.append((entry.name, sz))
    for name, sz in sorted(items, key=lambda x: x[1], reverse=True)[:10]:
        print(f"{name} - {human_size(sz)}")


if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else '.'
    top10(base)
