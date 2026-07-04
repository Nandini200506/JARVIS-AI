import pyttsx3

# Initialize the TTS engine only once
engine = pyttsx3.init()

# Set speaking rate
engine.setProperty("rate", 170)

# Set volume (0.0 to 1.0)
engine.setProperty("volume", 1.0)

# Select a voice (usually female on Windows)
voices = engine.getProperty("voices")

if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)
else:
    engine.setProperty("voice", voices[0].id)


def speak(text):
    """
    Convert text to speech.
    """

    if not text:
        return

    print(f"JARVIS: {text}")

    engine.say(text)
    engine.runAndWait()