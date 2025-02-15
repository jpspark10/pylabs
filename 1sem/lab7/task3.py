import requests
from config import API_KEY


def get_location_data(address):
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={address}&format=json"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            geo_object = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            full_address = geo_object["metaDataProperty"]["GeocoderMetaData"]["text"]
            coordinates = geo_object["Point"]["pos"]
            return full_address, coordinates
        except (IndexError, KeyError):
            return None, None
    else:
        print("Ошибка при выполнении запроса:", response.status_code)
        return None, None


def test():
    address = "Москва, Красная площадь, 1"

    full_address, coordinates = get_location_data(address)
    if full_address and coordinates:
        print(f"Полный адрес: {full_address}")
        print(f"Координаты: {coordinates}")
    else:
        print("Не удалось получить данные о местоположении.")


if __name__ == "__main__":
    test()
