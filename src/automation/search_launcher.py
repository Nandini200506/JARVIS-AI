import webbrowser
from urllib.parse import quote

def search_google(query):
    """
    Search anything on Google.
    Returns True if successful, otherwise False.
    """

    try:

        encoded_query = quote(query)

        url = f"https://www.google.com/search?q={encoded_query}"

        webbrowser.open(url)

        return True

    except Exception as e:

        print(f"Error: {e}")

        return False