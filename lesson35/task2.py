import requests
import json

def download_subreddit_comments(subreddit, save_path):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&sort=desc&size=1000"
    all_comments = []

    try:
        while True:
            response = requests.get(url)
            data = response.json()
            comments = data['data']
            if not comments:
                break
            all_comments.extend(comments)
            last_comment_timestamp = comments[-1]['created_utc']
            url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&sort=desc&size=1000&before={last_comment_timestamp}"
        
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(all_comments, f, ensure_ascii=False, indent=4)
        
        print(f"All comments from r/{subreddit} downloaded and saved to {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
subreddit = 'python'
save_path = 'python_comments.json'
download_subreddit_comments(subreddit, save_path)
