from brain.jarvis_brain import JarvisBrain
from nlp.entity_extractor import EntityExtractor
from tts.speaker import speak


class CommandRouter:
    """
    Routes user commands to the appropriate
    JARVIS functionality.
    """

    def __init__(self):
        self.brain = JarvisBrain()
        self.entity_extractor = EntityExtractor()

    def route(self, intent: str, command: str):
        """
        Route the detected intent.
        """

        if intent == "NEWS":

            self.brain.speak_news()

        elif intent == "WEATHER":

            city = self.entity_extractor.extract_city(command)

            self.brain.speak_weather(city)

        elif intent == "OPEN":

            if "notepad" in command:

                self.brain.open_notepad()

            elif "calculator" in command:

                self.brain.open_calculator()

            else:

                speak("I don't know that application.")

        elif intent == "EXIT":

            speak("Goodbye!")

            return False

        else:

            speak("Sorry, I don't understand that command.")

        return True