import requests
from bs4 import BeautifulSoup


def get_links_from_page(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Ошибка загрузки страницы: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    for a_tag in soup.find_all("a", href=True):
        links.append(a_tag["href"])

    return links


def test():
    base_url = "http://olympus.realpython.org/profiles"
    links = get_links_from_page(base_url)

    # Выводим ссылки
    print("Ссылки со страницы:")
    for link in links:
        print("http://olympus.realpython.org" + link)


if __name__ == "__main__":
    test()
