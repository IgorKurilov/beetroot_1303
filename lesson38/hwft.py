import aiohttp
import aiofiles
from bs4 import BeautifulSoup
import asyncio

# URL стартової сторінки документації
base_url = 'https://docs.python.org/3/library/index.html'

async def fetch_page(session, url):
    """
    Корутин для завантаження змісту сторінки за посиланням.
    """
    async with session.get(url) as response:
        return await response.text()

async def parse_page(content):
    """
    Корутин для парсингу змісту сторінки.
    """
    soup = BeautifulSoup(content, 'html.parser')
    return soup

async def save_content(title, content):
    """
    Корутин для збереження завантаженого контенту у файл.
    """
    filename = title.replace('/', '_') + '.txt'
    async with aiofiles.open(filename, 'w', encoding='utf-8') as file:
        await file.write(content)
    print(f"Зміст сторінки '{title}' збережено у файлі '{filename}'.")

async def main():
    async with aiohttp.ClientSession() as session:
        # Завантажити зміст головної сторінки
        index_content = await fetch_page(session, base_url)
        index_soup = await parse_page(index_content)

        # Знайти перші 10 посилань на основні документи
        main_links = index_soup.select('ul li.toctree-l1 > a')[:10]

        # Створити словник для зберігання назви та URL
        documents = {link.text: 'https://docs.python.org/3/library/' + link['href'] for link in main_links}

        # Створити конкурентні задачі для завантаження, парсингу та збереження контенту
        tasks = []
        for title, url in documents.items():
            tasks.append(asyncio.create_task(process_page(session, title, url)))

        await asyncio.gather(*tasks)

async def process_page(session, title, url):
    """
    Корутин для обробки сторінки: завантаження, парсинг і збереження.
    """
    page_content = await fetch_page(session, url)
    page_soup = await parse_page(page_content)
    
    # Знайти основний контент сторінки
    content_div = page_soup.find('div', {'class': 'body'})
    content = content_div.get_text(separator='\n') if content_div else 'No content found'
    
    await save_content(title, content)

if __name__ == "__main__":
    asyncio.run(main())
