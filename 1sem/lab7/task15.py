import requests
from bs4 import BeautifulSoup
import datetime


def search():
    my_list = []
    start = datetime.datetime.now()

    for i in range(1, 8):
        print(f'Поиск по {i} странице...')
        my_link = f'https://scrapingclub.com/exercise/list_basic/?page={i}/'
        html_text = requests.get(my_link).text
        soup = BeautifulSoup(html_text, "html.parser")
        quotes = soup.findAll('div', class_='w-full rounded border')
        for quote in quotes:
            soup2 = BeautifulSoup(requests.get(f'https://scrapingclub.com{quote.div.a['href']}').text, 'html.parser')

            price = quote.div.h5.get_text()
            title = quote.div.h4.a.get_text()
            photo = f'https://scrapingclub.com{quote.a.img['src']}'
            about = soup2.findAll('p', class_='card-description')[0].get_text()

            my_list.append({'title': title, 'about': about, 'photo': photo, 'price': float(price.strip('$'))})

    finish = datetime.datetime.now()
    print(f'Поиск окончен [Время работы {str(finish - start)}]\n')
    return my_list


def find_closest_product(products, target_price):
    closest_product = 0
    closest_price_diff = 1

    for product in products:
        price_diff = abs(product['price'] - target_price)
        if (price_diff < closest_price_diff or
                (price_diff == closest_price_diff and product['title'] < closest_product['title'])):
            closest_price_diff = price_diff
            closest_product = product

    return closest_product


if __name__ == "__main__":
    my_price = float(input("Введите цену: "))
    need_product = find_closest_product(search(), my_price)

    print(f'Найденный товар:\n'
          f'Название:\t{need_product['title']}\n'
          f'Описание:\t{need_product['about']}\n'
          f'Фотография:\t{need_product['photo']}\n'
          f'Цена:\t{need_product['price']}')
