import requests
import json
import time
import os
from datetime import datetime

# header
headers = {"User-Agent": "TrendPulse/1.0"}

# categories and keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# function to find category
def get_category(title):
    if not title:
        return None

    title = title.lower()

    for cat, words in categories.items():
        for word in words:
            if word in title:
                return cat
    return None


# get top story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Error fetching IDs")
    exit()

story_ids = response.json()[:50]

all_data = []

# loop category-wise
for cat in categories:
    count = 0

    for sid in story_ids:
        if count >= 25:
            break

        story_url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"

        try:
            res = requests.get(story_url, headers=headers)
            if res.status_code != 200:
                print("Error fetching story", sid)
                continue

            story = res.json()
        except:
            print("Request failed", sid)
            continue

        if not story:
            continue

        title = story.get("title", "")
        category = get_category(title)

        if category == cat:
            data = {
                "post_id": story.get("id"),
                "title": title,
                "category": cat,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            all_data.append(data)
            count += 1

    print(cat, "collected:", count)

    # sleep after each category
   # time.sleep(0.1)


# save file
os.makedirs("data", exist_ok=True)

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(all_data, f, indent=4)

print("\nCollected", len(all_data), "stories. Saved to", filename)