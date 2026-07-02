from brain.jarvis_brain import JarvisBrain


def main():
    """
    Entry point of the JARVIS AI Assistant.
    """

    brain = JarvisBrain()

    brain.speak_news()


if __name__ == "__main__":
    main()