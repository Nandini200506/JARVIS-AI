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

        application_aliases = {
            "notepad": "notepad",
            "calculator": "calculator",
            "calc": "calculator",
            "paint": "paint",
            "chrome": "chrome",
            "google chrome": "chrome",
            "vscode": "vscode",
            "vs code": "vscode",
            "visual studio code": "vscode",
            "spotify": "spotify"
        }

        for alias, app in application_aliases.items():
            if alias in command:
                return app

        return None
    def extract_website(self, command: str):
        """
        Extract website name from an OPEN command.
        """
        command = command.lower()

        website_aliases = {
            "google": "google",
            "youtube": "youtube",
            "github": "github",
            "git hub": "github",
            "gmail": "gmail",
            "chatgpt": "chatgpt",
            "chat gpt": "chatgpt",
            "linkedin": "linkedin",
            "linked in": "linkedin",
            "stackoverflow": "stackoverflow",
            "stack overflow": "stackoverflow"
        }

        for alias, website in website_aliases.items():
            if alias in command:
                return website

        return None
    def extract_folder(self, command: str):
        """
        Extract folder name from an OPEN command.
        """

        command = command.lower()

        folder_aliases = {
            "desktop": "desktop",
            "downloads": "downloads",
            "download": "downloads",
            "documents": "documents",
            "document": "documents",
            "pictures": "pictures",
            "picture": "pictures",
            "photos": "pictures",
            "music": "music",
            "songs": "music",
            "videos": "videos",
            "video": "videos"
        }

        for alias, folder in folder_aliases.items():
            if alias in command:
                return folder

        return None