import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import json
import time

SUBREDDIT = 'python'
URL = f"https://api.pushshift.io/reddit/comment/search/?subreddit={SUBREDDIT}&size=1000"

def fetch_comments(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    return []

def fetch_comments_threadpool(urls):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_comments, urls))
    return results

def fetch_comments_processpool(urls):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(fetch_comments, urls))
    return results

if __name__ == "__main__":
    urls = [URL] * 10  # Fetch 10 pages of comments

    # Using ThreadPoolExecutor
    start_time = time.time()
    comments_threadpool = fetch_comments_threadpool(urls)
    end_time = time.time()
    print(f"ThreadPoolExecutor fetched comments in {end_time - start_time} seconds")
    
    with open('comments_threadpool.json', 'w') as f:
        json.dump(comments_threadpool, f, indent=2)

    # Using ProcessPoolExecutor
    start_time = time.time()
    comments_processpool = fetch_comments_processpool(urls)
    end_time = time.time()
    print(f"ProcessPoolExecutor fetched comments in {end_time - start_time} seconds")
    
    with open('comments_processpool.json', 'w') as f:
        json.dump(comments_processpool, f, indent=2)
