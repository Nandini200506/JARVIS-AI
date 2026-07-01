import os
import requests

from dotenv import load_dotenv


class WeatherAPI:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str) -> dict | None:
        """
        Fetch weather information for a given city.

        Args:
            city (str): Name of the city.

        Returns:
            dict | None:
                Weather data if successful,
                otherwise None.
        """

        if not city.strip():
            print("Error: City name cannot be empty.")
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

            data = response.json()

            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }

            return weather_data

        except requests.exceptions.RequestException as error:

            print(f"Failed to fetch weather data: {error}")

            return None


if __name__ == "__main__":

    weather = WeatherAPI()

    data = weather.get_weather("Delhi")

    print(data)
    