import requests
import threading
import json

class CommentDownloader(threading.Thread):
    def __init__(self, url, results):
        threading.Thread.__init__(self)
        self.url = url
        self.results = results

    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            self.results.extend(data['data'])

def fetch_comments(subreddit):
    base_url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&size=100"
    results = []

    threads = [CommentDownloader(base_url + f"&before={i*100}", results) for i in range(10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    results.sort(key=lambda x: x['created_utc'])

    with open(f"{subreddit}_comments.json", "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    fetch_comments("python")
