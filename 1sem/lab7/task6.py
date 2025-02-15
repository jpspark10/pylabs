import requests
from config import API_KEY


def download_satellite_image(center_coordinates, size, zoom, output_file):
    base_url = (
        f"https://static-maps.yandex.ru/1.x/?"
        f"ll={center_coordinates}&"
        f"z={zoom}&"
        f"l=map&"
        f"size={size}"
    )

    response = requests.get(base_url)

    if response.status_code == 200:
        with open(output_file, "wb") as file:
            file.write(response.content)
        print(f"Снимок успешно сохранён в файл: {output_file}")
    elif response.status_code == 403:
        print("Ошибка 403: Проверьте корректность API-ключа и его доступность для Static API.")
    else:
        print(f"Ошибка загрузки изображения: {response.status_code}, причина: {response.text}")


def test():
    center_coordinates = "133.7751,-25.2744"
    size = "650,450"
    zoom = 4
    output_file = "australia_satellite.png"

    download_satellite_image(center_coordinates, size, zoom, output_file)


if __name__ == "__main__":
    test()
