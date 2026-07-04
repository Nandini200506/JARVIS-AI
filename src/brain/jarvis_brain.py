from api.weather_api import WeatherAPI
from api.news_api import NewsAPI
from automation.desktop_automation import DesktopAutomation
from tts.speaker import speak


class JarvisBrain:
    """
    Central Brain of the JARVIS AI Assistant.
    """

    def __init__(self):
        self.default_city = "Lucknow"

        self.weather = WeatherAPI()
        self.news = NewsAPI()
        self.desktop = DesktopAutomation()

    # ----------------------------
    # NEWS
    # ----------------------------

    def get_news(self, country="us", category=None, page_size=5):

        return self.news.get_top_headlines(
            country=country,
            category=category,
            page_size=page_size,
        )

    def speak_news(self):

        articles = self.get_news()

        if not articles:
            speak("Sorry, I could not fetch today's news.")
            return

        speak("Here are today's top headlines.")

        for index, article in enumerate(articles, start=1):

            title = article.get("title", "No title available")

            print(f"{index}. {title}")

            speak(title)

    # ----------------------------
    # WEATHER
    # ----------------------------

    def get_weather(self, city):

        data = self.weather.get_weather(city)

        if not data:
            return None

        try:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]

            return {
                "temp": temp,
                "condition": condition,
                "city": city,
            }

        except Exception:
            return None

    def speak_weather(self, city="Lucknow"):

        data = self.get_weather(city)

        if not data:
            speak("Sorry, I could not fetch weather data.")
            return

        response = (
            f"The temperature in {data['city']} is "
            f"{data['temp']} degrees with "
            f"{data['condition']}"
        )

        speak(response)

    # ----------------------------
    # DESKTOP AUTOMATION
    # ----------------------------

    def open_notepad(self):

        speak("Opening Notepad")

        self.desktop.open_notepad()

    def open_calculator(self):

        speak("Opening Calculator")

        self.desktop.open_calculator()