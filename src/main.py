from brain.jarvis_brain import JarvisBrain


def main():

    brain = JarvisBrain()

    articles = brain.get_news()

    if articles:

        print("\n========== JARVIS NEWS ==========\n")

        for index, article in enumerate(articles, start=1):

            print(f"{index}. {article['title']}")
            print(f"Source : {article['source']['name']}")
            print("-" * 80)


if __name__ == "__main__":
    main()