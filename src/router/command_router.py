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

            # Check desktop applications first
            app_name = self.entity_extractor.extract_application(command)

            if app_name:

                self.brain.open_application(app_name)

            else:

                # Check websites
                website_name = self.entity_extractor.extract_website(command)

                if website_name:

                    self.brain.open_website(website_name)

                else:

                    speak("I don't know that application or website.")

        elif intent == "EXIT":

            speak("Goodbye!")

            return False

        else:

            speak("Sorry, I don't understand that command.")

        return True