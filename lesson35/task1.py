import requests

def download_robots_txt(url, save_path):
    try:
        response = requests.get(url + '/robots.txt')
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"robots.txt downloaded from {url} and saved to {save_path}")
        else:
            print(f"Failed to download robots.txt from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
urls = ['https://en.wikipedia.org', 'https://twitter.com']
for url in urls:
    download_robots_txt(url, f"robots_{url.split('//')[1]}.txt")
