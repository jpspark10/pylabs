import requests

from lab7.config import API_KEY


def get_region(city):
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={city}&format=json"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            geo_object = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            region = geo_object["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
            for component in region:
                if component["kind"] == "province":
                    return component["name"]
            return "Область не найдена"
        except (IndexError, KeyError):
            return "Ошибка при обработке данных"
    else:
        return f"Ошибка запроса: {response.status_code}"


def test():
    cities = ["Барнаул", "Мелеуз", "Йошкар-Ола"]

    for city in cities:
        region = get_region(city)
        print(f"Город: {city}, Регион: {region}")


if __name__ == "__main__":
    test()
