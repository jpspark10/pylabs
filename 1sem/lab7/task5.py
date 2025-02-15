import requests
from config import API_KEY


def get_postal_code(address):
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={address}&format=json"

    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            geo_object = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            postal_code = geo_object["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
            return postal_code
        except (IndexError, KeyError):
            return "Почтовый индекс не найден"
    else:
        return f"Ошибка запроса: {response.status_code}"


def test():
    address = "Петровка, 38, Москва"
    postal_code = get_postal_code(address)
    print(f"Почтовый индекс для адреса '{address}': {postal_code}")


if __name__ == "__main__":
    test()
