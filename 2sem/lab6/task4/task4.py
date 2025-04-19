import os
import shutil
from datetime import datetime


def make_reserve_arc(source: str, dest: str):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(os.path.normpath(source))
    archive_name = f"{base_name}_{now}"
    dest_path = os.path.join(dest, archive_name)
    # создаём zip
    shutil.make_archive(dest_path, 'zip', source)
    print(f"Создан архив: {dest_path}.zip")


def main():
    print("Архивация каталога (резервное копирование)")
    source = input("Введите путь к исходному каталогу: ")
    dest = input("Введите путь к каталогу для сохранения архива: ")
    if not os.path.isdir(source):
        print(f"Источник не найден или не является каталогом: {source}")
        return
    if not os.path.isdir(dest):
        print(f"Каталог назначения не найден: {dest}")
        return
    try:
        make_reserve_arc(source, dest)
    except Exception as e:
        print(f"Ошибка при создании архива: {e}")


if __name__ == "__main__":
    main()
