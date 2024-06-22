import aiohttp
import aiofiles
import asyncio
import json

URL = "https://api.pushshift.io/reddit/comment/search/"

async def fetch_comments(session, url, params):
    async with session.get(url, params=params) as response:
        return await response.json()

async def save_comments_to_file(comments, filename):
    async with aiofiles.open(filename, 'w', encoding='utf-8') as file:
        await file.write(json.dumps(comments, indent=2))

async def main():
    params = {'subreddit': 'python', 'size': 1000, 'sort': 'asc'}
    async with aiohttp.ClientSession() as session:
        comments = await fetch_comments(session, URL, params)
        await save_comments_to_file(comments['data'], 'comments.json')

if __name__ == "__main__":
    asyncio.run(main())
