import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Read the NewsAPI key from the environment
api_key = os.getenv("NEWS_API_KEY")

# NewsAPI endpoint
url = "https://newsapi.org/v2/top-headlines"

# Query parameters
params = {
    "country": "us",      # Using 'us' because it returned news successfully
    "pageSize": 5,        # Fetch only 5 articles
    "apiKey": api_key
}

# Send GET request to NewsAPI
response = requests.get(url, params=params)

# Check whether the request was successful
if response.status_code == 200:

    # Convert JSON response into a Python dictionary
    data = response.json()

    # Get the list of articles
    articles = data["articles"]

    print("\n========== TOP HEADLINES ==========\n")

    # Print each headline
    for index, article in enumerate(articles, start=1):
        print(f"{index}. {article['title']}")
        print(f"Source : {article['source']['name']}")
        print(f"Author : {article['author']}")
        print(f"Published : {article['publishedAt']}")
        print(f"URL : {article['url']}")
        print("-" * 80)

else:
    print("Request Failed!")
    print("Status Code:", response.status_code)
    print(response.text)