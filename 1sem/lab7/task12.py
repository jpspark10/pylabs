import requests
from bs4 import BeautifulSoup
from collections import Counter


def get_authors(url):
    authors = []
    while url:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Ошибка загрузки страницы: {response.status_code}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        authors += [author.text for author in soup.select(".author")]

        next_button = soup.select_one(".next > a")
        url = "https://quotes.toscrape.com" + next_button["href"] if next_button else None

    return authors


def test():
    base_url = "https://quotes.toscrape.com/"
    authors = get_authors(base_url)

    author_counts = Counter(authors)

    sorted_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)

    print("Авторы, отсортированные по количеству цитат:")
    for author, count in sorted_authors:
        print(f"{author}: {count} цитат")


if __name__ == "__main__":
    test()
