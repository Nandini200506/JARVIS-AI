class EntityExtractor:

    def extract_city(self, command: str) -> str:

        command = command.lower().strip()

        if "weather in" in command:

            city = command.split("weather in", 1)[1].strip()

            if city:
                return city.title()

        return "Lucknow"


    def extract_application(self, command: str):
        """
        Extract application name from an OPEN command.
        """

        command = command.lower()

        applications = [
            "notepad",
            "calculator",
            "paint",
            "chrome",
            "vscode",
            "spotify"
        ]

        for app in applications:
            if app in command:
                return app

        return None