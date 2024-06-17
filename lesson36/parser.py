import requests
from bs4 import BeautifulSoup

# URL стартової сторінки документації
base_url = 'https://docs.python.org/3/library/index.html'
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Знайти перші 10 посилань на основні документи
main_links = soup.select('ul li.toctree-l1 > a')[:10]

# Створити словник для зберігання назви та URL
documents = {link.text: 'https://docs.python.org/3/library/' + link['href'] for link in main_links}

# Завантажити зміст кожної сторінки та зберегти у окремі файли
for title, url in documents.items():
    # Видалити слеші з назви, щоб вони не впливали на ім'я файлу
    filename = title.replace('/', '_') + '.txt'
    response = requests.get(url)
    page_soup = BeautifulSoup(response.content, 'html.parser')

    # Знайти основний контент сторінки
    content_div = page_soup.find('div', {'class': 'body'})
    content = content_div.get_text(separator='\n') if content_div else 'No content found'

    # Записати контент у файл
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Зміст сторінки '{title}' збережено у файлі '{filename}'.")

print("Завантаження завершено.")
