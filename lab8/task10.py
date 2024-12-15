import asyncio
import requests
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from lab8.config import BOT_TOKEN, YANDEX_API_KEY_GEOCODER

YANDEX_API_KEY = YANDEX_API_KEY_GEOCODER
YANDEX_GEOCODER_URL = "https://geocode-maps.yandex.ru/1.x/"
YANDEX_STATIC_MAP_URL = "https://static-maps.yandex.ru/1.x/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_bot(message: Message):
    await message.answer("Добро пожаловать! Отправьте мне название места, и я пришлю карту с его расположением.")


@dp.message()
async def handle_location_request(message: Message):
    location_name = message.text.strip()
    print(location_name)

    try:
        geocoder_params = {
            "apikey": YANDEX_API_KEY,
            "geocode": location_name,
            "format": "json"
        }
        geocoder_response = requests.get(YANDEX_GEOCODER_URL, params=geocoder_params)
        geocoder_response.raise_for_status()
        geocoder_data = geocoder_response.json()

        geo_objects = geocoder_data["response"]["GeoObjectCollection"]["featureMember"]
        if not geo_objects:
            await message.answer("К сожалению, ничего не найдено. Попробуйте уточнить запрос.")
            return

        geo_object = geo_objects[0]["GeoObject"]
        coords = geo_object["Point"]["pos"].split()
        lon, lat = coords[0], coords[1]
        description = geo_object["metaDataProperty"]["GeocoderMetaData"]["text"]

        static_map_params = {
            "l": "map",
            "pt": f"{lon},{lat},pm2rdm",
            "size": "450,450",
            "lang": "ru_RU"
        }
        map_url = f"{YANDEX_STATIC_MAP_URL}?" + "&".join(f"{key}={value}" for key, value in static_map_params.items()) + "&z=15"
        print(map_url)

        await message.answer_photo(
            photo=map_url,
            caption=f"Найденный объект: {description}"
        )
    except requests.exceptions.RequestException as e:
        await message.answer(f"Произошла ошибка при выполнении запроса: {e}")
    except Exception as e:
        await message.answer(f"Произошла непредвиденная ошибка: {e}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
