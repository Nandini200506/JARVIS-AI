class IntentDetector:
    """
    Detects the user's intent from a spoken command.

    Currently uses rule-based NLP with keyword matching.

    This class is designed so that the internal
    implementation can later be replaced by
    Machine Learning or an LLM without changing
    the rest of the application.
    """

    def __init__(self):
        """
        Initialize the Intent Knowledge Base.
        """

        self.intents = {

            "NEWS": [
                "news",
                "headline",
                "headlines",
                "latest news",
                "breaking news",
                "today news",
                "today's news"
            ],

            "WEATHER": [
                "weather",
                "temperature",
                "forecast",
                "rain",
                "climate",
                "weather today",
                "weather in"
            ],

            "OPEN": [
                "open",
                "launch",
                "start",
                "run"
            ],

            "SEARCH": [
                "search",
                "google",
                "look up",
                "find",
                "search for"
            ],
            "TIME": [
                "time",
                "current time",
                "what time is it",
                "tell me the time",
                "time now"
            ],
            "DATE": [
                "date",
                "today's date",
                "today date",
                "current date",
                "what is today's date",
                "tell me today's date"
            ],

            "DAY": [
                "day",
                "today's day",
                "what day is today",
                "which day is today",
                "current day"
            ],
            "VOLUME_UP": [
                "increase volume",
                "volume up",
                "raise volume",
                "increase sound",
                "sound up"
            ],
            "VOLUME_DOWN": [
                "decrease volume",
                "volume down",
                "down volume",
                "decrease sound",
                "sound down"
            ],

            "MUTE": [
                "mute",
                "mute volume",
                "mute sound",
                "turn off sound",
                "turn off volume"
            ],

            "EXIT": [
                "exit",
                "quit",
                "stop",
                "bye",
                "goodbye",
                "shutdown"
            ]
        }

    def detect_intent(self, command: str) -> str:
        """
        Detect the intent from a user command.

        Args:
            command (str):
                Spoken command.

        Returns:
            str:
                Detected intent.
        """

        command = command.lower()

        for intent, keywords in self.intents.items():

            for keyword in keywords:

                if keyword in command:
                    return intent

        return "UNKNOWN"