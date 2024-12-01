import requests
from bs4 import BeautifulSoup
import random


def get_all_quotes(url):
    quotes = []
    while url:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Ошибка загрузки страницы: {response.status_code}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        quote_elements = soup.select(".quote")
        for element in quote_elements:
            text = element.select_one(".text").text
            author = element.select_one(".author").text
            quotes.append((text, author))

        next_button = soup.select_one(".next > a")
        url = "https://quotes.toscrape.com" + next_button["href"] if next_button else None

    return quotes


def test():
    base_url = "https://quotes.toscrape.com/"
    all_quotes = get_all_quotes(base_url)

    random_quotes = random.sample(all_quotes, 5)

    print("Пять случайных цитат:")
    for text, author in random_quotes:
        print(f'{text} - {author}')


if __name__ == "__main__":
    test()
