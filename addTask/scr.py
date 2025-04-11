import requests
# Библиотека requests используется для выполнения HTTP-запросов. Она позволяет отправлять запросы на сервер и получать ответы.
from bs4 import BeautifulSoup
# Библиотека BeautifulSoup используется для анализа (парсинга) HTML-кода
# Она позволяет легко находить элементы по их классам, тегам или атрибутам
import pandas as pd

def fetch_page_content(url):
    """
    Получает HTML-контент страницы по указанному URL.
    :param url: URL страницы для запроса
    :return: Текстовое содержимое страницы
    """
    try:
#       Многие сайты проверяют заголовок User-Agent, чтобы определить, является ли запрос от браузера или от скрипта
# Если не указать User-Agent, некоторые сайты могут заблокировать запрос или вернуть пустую страницу
# имитируем запрос от браузера Google Chrome, указывая соответствую
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
#         Метод requests.get отправляет GET-запрос на указанный url.
# передаем заголовки (headers) вместе с запросом, чтобы сайт "думал", что запрос исходит от реального пользователя
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        # Атрибут response.text содержит текстовый HTML-код страницы
# Этот код будет использован для парсинга данных с помощью библиотеки BeautifulSoup
        return response.text
        # если ошика то прекращается выполнение программы
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return None
def parse_news_from_page(html):
    """
    Парсит заголовки, даты, теги и ссылки на новости из HTML-кода страницы
    :param html: HTML страницы
    :return: Список словарей содержит данные о новости
    """
#     Объект BeautifulSoup преобразует HTML-код в дерево элементов, которое можно легко анализировать.
# Параметр 'html.parser' указывает, что используется встроенный HTML-парсер Python
    soup = BeautifulSoup(html, 'html.parser')
    news_list = []

    # Метод find_all ищет все элементы с тегом <article> и классом tm-articles-list__item
    articles = soup.find_all('article', class_='tm-articles-list__item')
    if not articles:
        print("ооооошшииббкккааа")
        return news_list

    for article in articles:
        # Заголовок новост
#         Метод find ищет первый элемент с тегом <a> и классом tm-title__link внутри текущей статьи.
# Если заголовок найден, мы извлекаем его текст с помощью .text.strip() (убираем лишние пробелы).
# Если заголовок не найден, устанавливаем значение "No Title".
        title_tag = article.find('a', class_='tm-title__link')
        title = title_tag.text.strip() if title_tag else "нету"

        # Ссылка на новость
        link = "https://habr.com" + title_tag['href'] if title_tag else "No Link"

        # Дата публикации
#         Метод find ищет элемент с тегом <time>, который содержит дату публикации.
# Атрибут datetime содержит дату в формате ISO (2023-10-01T12:34:56Z).
# Если дата не найдена, устанавливаем значение "нет"
        date_tag = article.find('time')
        date = date_tag['datetime'] if date_tag else "нет"

         # Теги
#         Метод find ищет контейнер с классом tm-publication-hubs__container, который содержит теги
# Если контейнер найден, мы используем find_all для поиска всех ссылок с классом tm-publication-hub__link
# Для каждой ссылки извлекаем текст и объединяем теги через запятую с помощью ", ".join(tags)
        tags_container = article.find('div', class_='tm-publication-hubs__container')  # Контейнер с тегами
        tags = [tag.text.strip() for tag in tags_container.find_all('a', class_='tm-publication-hub__link')]
        tags = ", ".join(tags) if tags else "нет"

        # Добавляем данные в список
        # словарь с данными о новости (заголовок, ссылка, дата, теги) и добавляем его в список
        news_list.append({
            'title': title,
            'link': link,
            'date': date,
            'tags': tags
        })

        # print(f"Дата публикации: {date}")
        # print(f"Заголовок: {title}")
        # print(f"Ссылка: {link}")
        # print(f"Дата: {text}")
        # print(f"Теги: {tags}")
        # print("-" * 20)
# Функция возвращает список словарей, где каждый словарь содержит данные о новости
    return news_list

def fetch_news_text(url):
    """
    Получает текст полной новости по ссылке.
    :param url: URL новости
    :return: Текст новости
    """
    try:
#       Функция fetch_page_content получает HTML-код страницы.
# Функция parse_news_from_page анализирует HTML и извлекает данные о новостях.
        html = fetch_page_content(url)
        if not html:
            return "ннетуууууу"
            # Создает объект BeautifulSoup для анализа HTML-кода страницы.
# Ищет все блоки текста новости.
# Объединяет найденные блоки в одну строку.

        soup = BeautifulSoup(html, 'html.parser')

        # Находим текст новости
        text_blocks = soup.find_all('div', class_='article-formatted-body')
        #         Для каждого найденного блока (block) извлекается текст с помощью .text.strip():
# .text возвращает текстовое содержимое элемента.
# .strip() удаляет лишние пробелы и переносы строк в начале и конце текста
        full_text = "\n".join([block.text.strip() for block in text_blocks])
        return full_text if full_text else "No Text"
    except Exception as e:
        print(f"Ошибка ")
        return "нетттттт"


def main():
    """
    Основная функция программы.
    Собирает данные о новостях с нескольких страниц Хабра и сохраняет их в DataFramк
    """
    # {} будет заменен
    base_url = "https://habr.com/ru/all/page{}/"
    all_news = []

    for page_num in range(1, 7):
        print(f"Обработана {page_num} страница")
#         Метод .format(page_num) заменяет {} в base_url на текущий номер страницы.
        url = base_url.format(page_num)
        # Функция fetch_page_content отправляет HTTP-запрос на указанный URL и возвращает HTML-код страницы
        html = fetch_page_content(url)

# Функция parse_news_from_page анализирует HTML-код и извлекает данные о новостях (заголовки, ссылки, данных, теги)
# Результат — список словарей, где каждый словарь содержит данные о новости.
        if html:
            news_list = parse_news_from_page(html)
            if not news_list:
                print(f"На странице {page_num} нет новостейййййййййй")
                continue
#                 Для каждой новости из списка news_list:
# Вызывается функция fetch_news_text, которая извлекает полный текст новости по её ссылке.
# Полный текст добавляется в словарь новости как новый ключ 'text'
# Словарь с данными о новости добавляется в общий список all_news
            for news in news_list:
                # Добавляем текст новости
                news['text'] = fetch_news_text(news['link'])
                all_news.append(news)

    # Создаем DataFrame из собранных данных
    df = pd.DataFrame(all_news)

    # Сохраняем данные в CSV файл
    df.to_csv("habr_news.csv", index=False, encoding='utf-8')
    print("всо!")

if __name__ == "__main__":
    main()