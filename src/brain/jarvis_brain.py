from api.weather_api import WeatherAPI
from api.news_api import NewsAPI


class JarvisBrain:
    """
    Central brain of the JARVIS AI Assistant.

    This class coordinates different modules such as
    Weather, News, Calculator, etc.
    """

    def __init__(self):

        self.weather = WeatherAPI()

        self.news = NewsAPI()

    def get_news(
        self,
        country="us",
        category=None,
        page_size=5
    ):
        """
        Fetch top news headlines.
        """

        return self.news.get_top_headlines(
            country=country,
            category=category,
            page_size=page_size
        )