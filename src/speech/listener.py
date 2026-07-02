import speech_recognition as sr


class SpeechListener:
    """
    Converts voice input into text for JARVIS.
    """

    def __init__(self):

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        """
        Listen to user voice and convert it into text.
        """

        with self.microphone as source:

            print("🎤 Listening...")

            # adjust for background noise
            self.recognizer.adjust_for_ambient_noise(source)

            audio = self.recognizer.listen(source)

        try:
            print("🧠 Recognizing...")

            text = self.recognizer.recognize_google(audio)

            text = text.lower()

            print(f"YOU SAID: {text}")

            return text

        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return None

        except sr.RequestError:
            print("❌ Speech service error")
            return None