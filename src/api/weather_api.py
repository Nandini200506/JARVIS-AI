import os
import requests

from dotenv import load_dotenv


class WeatherAPI:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str = "Lucknow"):
        """
        Fetch weather data from OpenWeather API.
        """

        if not self.api_key:
            print("Error: WEATHER_API_KEY not found.")
            return None

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:

            response = requests.get(
                self.base_url,
                params=params
            )

            

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as error:

            print(f"Weather API Error: {error}")

            return None


if __name__ == "__main__":

    weather = WeatherAPI()

    data = weather.get_weather("Delhi")

    print(data)
    