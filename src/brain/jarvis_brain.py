from api.weather_api import WeatherAPI
from api.news_api import NewsAPI
from automation.desktop_automation import DesktopAutomation
from tts.speaker import speak
from automation.app_launcher import launch_application
from automation.website_launcher import launch_website
from automation.file_launcher import open_folder as launch_folder
from automation.search_launcher import search_google as launch_search
from utils.time_manager import TimeManager

class JarvisBrain:
    """
    Central Brain of the JARVIS AI Assistant.
    """

    def __init__(self):
        self.default_city = "Lucknow"

        self.weather = WeatherAPI()
        self.news = NewsAPI()
        self.desktop = DesktopAutomation()
        self.time_manager = TimeManager()

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
    
    def open_application(self, app_name):
        """
        Opens an application using the Smart Application Launcher.
        """

        if launch_application(app_name):

            speak(f"Opening {app_name}")

        else:

            speak(f"Sorry, I couldn't open {app_name}")
    
    def open_website(self, website_name):
        """
        Opens a website in the default browser.
        """

        if launch_website(website_name):

            speak(f"Opening {website_name}")

        else:

            speak(f"Sorry, I couldn't open {website_name}")
        
    def open_folder(self, folder_name):
        """
        Opens a folder from the Smart File Launcher.
        """

        if launch_folder(folder_name):

            speak(f"Opening {folder_name}")

        else:

            speak(f"Sorry, I couldn't open {folder_name}")

    def search_google(self, query):
            """
            Searches Google for the given query.
            """

            if launch_search(query):

                speak(f"Searching Google for {query}")

            else:

                speak("Sorry, I couldn't perform the search.")
    
    def speak_current_time(self):
        """
        Speaks the current time.
        """

        current_time = self.time_manager.get_current_time()

        speak(f"The current time is {current_time}") 

    def speak_current_date(self):
        """
        Speaks the current date.
        """

        current_date = self.time_manager.get_current_date()

        speak(f"Today's date is {current_date}")     

    def speak_current_day(self):
        """
        Speaks the current day.
        """

        current_day = self.time_manager.get_current_day()

        speak(f"Today is {current_day}")