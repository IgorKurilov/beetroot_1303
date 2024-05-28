# results.py

def save_results(player_name, score):
    """Save player's results to a file."""
    with open('results.txt', 'a') as file:
        file.write(f"{player_name}: {score}\n")

def get_top_results():
    """Get top 5 results from the file."""
    results = []
    with open('results.txt', 'r') as file:
        lines = file.readlines()
        lines.sort(reverse=True, key=lambda x: int(x.split(': ')[1]))
        for line in lines[:5]:
            results.append(line.strip())
    return results

