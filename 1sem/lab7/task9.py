import requests
from config import API_KEY


def get_city_coordinates(city_name):
    base_url = f"https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": API_KEY,
        "geocode": city_name,
        "format": "json"
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        result = response.json()
        try:
            pos = result["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            lon, lat = map(float, pos.split())
            return lat
        except (IndexError, KeyError, ValueError):
            print(f"Не удалось получить координаты для города {city_name}.")
            return None
    else:
        print(f"Ошибка запроса для города {city_name}: {response.status_code}")
        return None


def find_southernmost_city(cities):
    southernmost_city = None
    southernmost_latitude = float('inf')

    for city in cities:
        latitude = get_city_coordinates(city)
        if latitude is not None and latitude < southernmost_latitude:
            southernmost_latitude = latitude
            southernmost_city = city

    return southernmost_city


def test():
    cities_input = input("Введите список городов через запятую: ")
    cities = [city.strip() for city in cities_input.split(",")]

    southernmost_city = find_southernmost_city(cities)
    if southernmost_city:
        print(f"Самый южный город: {southernmost_city}")
    else:
        print("Не удалось определить самый южный город.")


if __name__ == "__main__":
    test()
