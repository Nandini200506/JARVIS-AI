class EntityExtractor:
    """
    Extracts important entities from user commands.

    Examples:
        weather in delhi      -> Delhi
        weather in mumbai     -> Mumbai
        weather in new york   -> New York
    """

    def extract_city(self, command: str) -> str:
        """
        Extract city name from a weather command.
        """

        command = command.lower().strip()

        if "weather in" in command:

            city = command.split("weather in", 1)[1].strip()

            if city:
                return city.title()

        # Default city
        return "Lucknow"