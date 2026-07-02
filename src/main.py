from speech.listener import SpeechListener
from brain.jarvis_brain import JarvisBrain


def get_intent(command: str):

    command = command.lower()

    # NEWS INTENT
    if any(word in command for word in ["news", "headlines", "updates"]):
        return "NEWS"

    # WEATHER INTENT
    elif any(word in command for word in ["weather", "temperature", "climate"]):
        return "WEATHER"

    # EXIT INTENT
    elif any(word in command for word in ["exit", "stop", "shutdown", "bye"]):
        return "EXIT"

    else:
        return "UNKNOWN"


def main():

    listener = SpeechListener()
    brain = JarvisBrain()

    print("🤖 JARVIS SMART MODE ACTIVE")

    while True:

        command = listener.listen()

        if command is None:
            continue

        print("RAW COMMAND:", command)

        intent = get_intent(command)

        print("INTENT:", intent)

        # ROUTING SYSTEM
        if intent == "NEWS":
            brain.speak_news()

        elif intent == "WEATHER":
            brain.speak_weather()

    

        elif intent == "EXIT":
            print("JARVIS SHUTTING DOWN")
            break

        else:
            print("Sorry, I didn't understand that command.")


if __name__ == "__main__":
    main()