from speech.listener import SpeechListener
from router.command_router import CommandRouter
from nlp.intent_detector import IntentDetector


def main():
    """
    Main entry point of JARVIS AI.
    """

    listener = SpeechListener()
    detector = IntentDetector()
    router = CommandRouter()

    print("🤖 JARVIS IS NOW ACTIVE")

    while True:

        command = listener.listen()

        if not command:
            continue

        print(f"RAW COMMAND: {command}")

        intent = detector.detect_intent(command)

        print(f"INTENT: {intent}")

        should_continue = router.route(intent, command)

        if not should_continue:
            print("JARVIS SHUTTING DOWN")
            break


if __name__ == "__main__":
    main()