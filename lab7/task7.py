import requests


def download_map_with_marks(center_coordinates, zoom, size, marks, output_file):
    placemarks = "pt=" + "".join(
        [f"{mark['coordinates']},{mark['style']}" for mark in marks]
    )

    base_url = (
        f"https://static-maps.yandex.ru/1.x/?"
        f"ll={center_coordinates}&"
        f"z={zoom}&"
        f"l=map&"
        f"size={size}&"
        f"{placemarks}"
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
    center_coordinates = "86.087314,55.354968"
    zoom = 11
    size = "650,450"
    marks = [
        {"coordinates": "86.071048,55.344957", "style": "pm2dgl~"},
        {"coordinates": "86.078502,55.339750", "style": "pm2rdl~"},
        {"coordinates": "86.089139,55.357639", "style": "pm2ywl~"},
        {"coordinates": "86.075950,55.363284", "style": "pm2vvl"}
    ]
    output_file = "kemerovo_map_with_marks.png"
    download_map_with_marks(center_coordinates, zoom, size, marks, output_file)


if __name__ == "__main__":
    test()
