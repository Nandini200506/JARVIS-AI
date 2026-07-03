from speech.listener import SpeechListener
from router.command_router import CommandRouter


def detect_intent(command: str) -> str:
    """
    Detect the user's intent based on the spoken command.
    """

    command = command.lower()

    if "news" in command:
        return "NEWS"

    elif "weather" in command:
        return "WEATHER"

    elif command in ["exit", "quit", "stop", "bye"]:
        return "EXIT"

    return "UNKNOWN"


def main():
    """
    Main function of JARVIS AI.
    """

    listener = SpeechListener()
    router = CommandRouter()

    print("🤖 JARVIS IS NOW ACTIVE")

    while True:

        command = listener.listen()

        if not command:
            continue

        print(f"RAW COMMAND: {command}")

        intent = detect_intent(command)

        print(f"INTENT: {intent}")

        should_continue = router.route(intent, command)

        if not should_continue:
            print("JARVIS SHUTTING DOWN")
            break


if __name__ == "__main__":
    main()