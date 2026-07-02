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
        self.default_city = "Lucknow"

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



    def get_weather(self, city: str = "Lucknow"):
        """
        Fetch weather data from Weather API.
        """
       
        data = self.weather.get_weather(city)

        if not data:
            return None

        try:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]

            return {
                "temp": temp,
                "condition": condition,
                "city": city
            }

        except Exception:
            return None
    

    def speak_weather(self, city: str = "Lucknow"):
        """
        Speak weather information.
        """

        data = self.get_weather(city)

        if not data:
            self.speaker.speak("Sorry, I could not fetch weather data.")
            return

        response = f"The temperature in {data['city']} is {data['temp']} degrees with {data['condition']}"

        self.speaker.speak(response)