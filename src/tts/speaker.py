import pyttsx3


class Speaker:
    """
    Handles Text-to-Speech for JARVIS.
    """

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)

        self.engine.setProperty("volume", 1.0)

    def add_to_queue(self, text: str):
        """
        Add text to the speech queue.
        """

        if not text:
            return

        print(f"JARVIS: {text}")

        self.engine.say(text)

    def speak_queue(self):
        """
        Speak everything in the queue.
        """

        self.engine.runAndWait()

    def speak(self, text: str):
        """
        Speak a single sentence.
        """

        self.add_to_queue(text)

        self.speak_queue()