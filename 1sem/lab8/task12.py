import asyncio
import aiohttp
from bs4 import BeautifulSoup
from telegram.ext import CommandHandler, Application

import datetime

from lab8.config import BOT_TOKEN


async def search():
    my_list = []
    for i in range(1, 7):
        print(f'Поиск по {i} странице...')
        my_link = f'https://scrapingclub.com/exercise/list_basic/?page={i}'
        my_list.append(my_link)

    async with aiohttp.ClientSession() as session:
        tasks = [get_url(url, session) for url in my_list]
        results = await asyncio.gather(*tasks)
        return [item for sublist in results for item in sublist]


async def get_url(url, session):
    async with session.get(url) as resp:
        html_text = await resp.text()
        soup = BeautifulSoup(html_text, "html.parser")
        quotes = soup.findAll('div', class_='w-full rounded border')
        product_list = []

        for quote in quotes:
            product_url = f'https://scrapingclub.com{quote.div.a["href"]}'
            async with session.get(product_url) as product_resp:
                product_html = await product_resp.text()
                soup2 = BeautifulSoup(product_html, 'html.parser')
                price = quote.div.h5.get_text()
                title = quote.div.h4.a.get_text()
                photo = f'https://scrapingclub.com{quote.a.img["src"]}'
                about = soup2.findAll('p', class_='card-description')[0].get_text()

                product_list.append({
                    'title': title,
                    'about': about,
                    'photo': photo,
                    'price': float(price.strip('$'))
                })

        return product_list


def find_closest_product(products, target_price):
    sorted_products = sorted(products, key=lambda product: (abs(target_price - product['price']), product['title']))
    return sorted_products[0]


async def find_price(update, context):
    if not context.args:
        await update.message.reply_text('Пожалуйста, укажите цену.')
        return

    start_t = datetime.datetime.now()

    await update.message.reply_text('Начинаем поиск...')
    context.user_data['user_price'] = float(context.args[0])
    products = await search()
    context.user_data['product'] = find_closest_product(products, context.user_data['user_price'])

    await context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=context.user_data["product"]["photo"],
        caption=(
            f'Название: {context.user_data["product"]["title"]}\n\n'
            f'Описание:\n{context.user_data["product"]["about"]}\n\n'
            f'Цена: {context.user_data["product"]["price"]}$'
        )
    )

    finish = datetime.datetime.now()
    print(f'Поиск окончен [Время работы {str(finish - start_t)}]\n')


async def start(update, context):
    await update.message.reply_text('Введите требуемую цену: /price <ваша_цена>')


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("price", find_price))

    application.run_polling()


if __name__ == '__main__':
    main()
