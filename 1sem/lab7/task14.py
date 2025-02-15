import requests
from bs4 import BeautifulSoup


def get_quotes_by_tags(tags):
    base_url = "https://quotes.toscrape.com/tag/"
    quotes = []

    for tag in tags:
        url = f"{base_url}{tag}/"
        while url:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Ошибка загрузки страницы для тега {tag}: {response.status_code}")
                break

            soup = BeautifulSoup(response.text, "html.parser")

            quote_elements = soup.select(".quote")
            for element in quote_elements:
                text = element.select_one(".text").text
                author = element.select_one(".author").text
                quotes.append((tag, text, author))

            next_button = soup.select_one(".next > a")
            url = f"https://quotes.toscrape.com{next_button['href']}" if next_button else None

    return quotes


def test():
    tags = input("Введите теги через запятую: ").split(",")
    tags = [tag.strip() for tag in tags]

    all_quotes = get_quotes_by_tags(tags)

    if not all_quotes:
        print("Цитаты с указанными тегами не найдены.")
    else:
        print("\nЦитаты с указанными тегами:")
        for tag, text, author in all_quotes:
            print(f"[{tag}] \"{text}\" - {author}")


if __name__ == "__main__":
    test()
