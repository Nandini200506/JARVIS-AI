from api.weather_api import WeatherAPI
from api.news_api import NewsAPI
from tts.speaker import Speaker


class JarvisBrain:
    """
    Central Brain of the JARVIS AI Assistant.

    This class coordinates different modules like:
    - Weather
    - News
    - Speaker
    """

    def __init__(self):
        """
        Initialize all modules.
        """

        self.weather = WeatherAPI()

        self.news = NewsAPI()

        self.speaker = Speaker()

    def get_news(
        self,
        country="us",
        category=None,
        page_size=5
    ):
        """
        Fetch latest news headlines.
        """

        return self.news.get_top_headlines(
            country=country,
            category=category,
            page_size=page_size
        )

    def speak_news(self):
        """
        Fetch and speak the latest news headlines.
        """

        articles = self.get_news()

        if not articles:
            self.speaker.speak("Sorry, I could not fetch today's news.")
            return

        self.speaker.add_to_queue("Here are today's top headlines.")

        for index, article in enumerate(articles, start=1):

            title = article.get("title", "No title available")

            print(f"{index}. {title}")

            self.speaker.add_to_queue(title)

        self.speaker.speak_queue()