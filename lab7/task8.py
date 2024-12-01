import requests
from config import API_KEY  # Импортируем API-ключ из config.py


def download_map_with_route(center_coordinates, zoom, size, route_points, output_file):
    """
    Загружает карту с заданным маршрутом и сохраняет в файл.
    """
    # Формируем строку с маршрутом
    route = ",".join(route_points)

    # Формируем URL для запроса
    base_url = (
        f"https://static-maps.yandex.ru/1.x/?"
        f"pl={route}&"
        f"ll={center_coordinates}&"
        f"z={zoom}&"
        f"l=map&"
        f"size={size}"
    )

    print(base_url)
    response = requests.get(base_url)

    if response.status_code == 200:
        with open(output_file, "wb") as file:
            file.write(response.content)
        print(f"Карта успешно сохранена в файл: {output_file}")
    elif response.status_code == 403:
        print("Ошибка 403: Проверьте корректность API-ключа и его доступность для Static API.")
    else:
        print(f"Ошибка загрузки карты: {response.status_code}, причина: {response.text}")


def test():
    center_coordinates = "86.2,54.5"  # Центр Кемеровской области
    zoom = 6  # Масштаб карты для отображения области
    size = "650,450"  # Размер карты (ширина, высота)
    route_points = [
        "86.087314,55.354968",  # Кемерово
        "86.178149,54.667588",  # Ленинск-Кузнецк
        "87.123498,53.755669",  # Новокузнецк
        "87.988543,52.920602"  # Шерегеш
    ]
    output_file = "kemerovo_area_with_route.png"
    download_map_with_route(center_coordinates, zoom, size, route_points, output_file)


if __name__ == "__main__":
    test()
