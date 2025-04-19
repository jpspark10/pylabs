import zipfile
from collections import defaultdict


def human_size(num_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(num_bytes)
    idx = 0
    while size >= 1024 and idx < len(units) - 1:
        size /= 1024
        idx += 1
    return f"{round(size)}{units[idx]}"


def build_tree(infolist):
    Tree = lambda: defaultdict(Tree)
    root = Tree()
    sizes = {}
    for info in infolist:
        if info.filename.endswith('/'):
            continue
        path = info.filename
        parts = path.split('/')
        cur = root
        for p in parts[:-1]:
            cur = cur[p]
        cur[parts[-1]] = None
        sizes[path] = info.file_size
    return root, sizes


def print_tree(node, sizes, indent=0):
    for key in sorted(node.keys()):
        if node[key] is None:
            sz = sizes.get(f"{key}" if indent == 0 else None, sizes.get(key, 0))
            print("  " * indent + f"{key} {human_size(sizes.get('/'.join(get_path(node, key)), 0))}")
        else:
            # выводим каталог
            print("  " * indent + key)
            print_tree(node[key], sizes, indent + 1)


def get_path(node, key):
    return [key]


def main():
    archive = input("Введите путь к zip-архиву: ")
    try:
        with zipfile.ZipFile(archive) as zf:
            tree, sizes = build_tree(zf.infolist())
            print_tree(tree, sizes)
    except FileNotFoundError:
        print(f"Файл не найден: {archive}")
    except zipfile.BadZipFile:
        print(f"Некорректный zip-архив: {archive}")


if __name__ == "__main__":
    main()
