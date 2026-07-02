import os
import requests

from dotenv import load_dotenv


class NewsAPI:
    """
    Handles fetching news headlines from NewsAPI.
    """

    def __init__(self):
        load_dotenv()

        self.api_key = os.getenv("NEWS_API_KEY")

        self.base_url = "https://newsapi.org/v2/top-headlines"

    def get_top_headlines(
        self,
        country="us",
        category=None,
        page_size=5
    ):

        if not self.api_key:
            print("NEWS_API_KEY not found.")
            return None

        params = {
            "country": country,
            "pageSize": page_size,
            "apiKey": self.api_key
        }

        if category:
            params["category"] = category

        try:

            response = requests.get(
                self.base_url,
                params=params,
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            return data.get("articles", [])

        except requests.exceptions.RequestException as e:

            print(f"Error: {e}")

            return None


if __name__ == "__main__":

    news = NewsAPI()

    articles = news.get_top_headlines()

    if articles:

        print("\n========== TOP HEADLINES ==========\n")

        for index, article in enumerate(articles, start=1):

            print(f"{index}. {article['title']}")
            print(f"Source : {article['source']['name']}")
            print(f"URL : {article['url']}")
            print("-" * 80)