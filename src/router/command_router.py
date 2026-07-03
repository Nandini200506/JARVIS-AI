from brain.jarvis_brain import JarvisBrain


class CommandRouter:
    """
    Routes user commands to the appropriate
    JARVIS functionality.
    """

    def __init__(self):
        """
        Initialize the router.
        """

        self.brain = JarvisBrain()

    def route(self, intent: str, command: str):
        """
        Route the detected intent.

        Args:
            intent (str): Detected intent.
            command (str): Original voice command.
        """

        if intent == "NEWS":

            self.brain.speak_news()

        elif intent == "WEATHER":

            city = self.brain.default_city

            if "weather in" in command:
                city = command.split("weather in")[-1].strip()

            self.brain.speak_weather(city)

        elif intent == "EXIT":

            self.brain.speaker.speak("Goodbye!")

            return False

        else:

            self.brain.speaker.speak(
                "Sorry, I don't understand that command."
            )

        return True