import webbrowser
WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chat.openai.com",
    "linkedin": "https://www.linkedin.com",
    "stackoverflow": "https://stackoverflow.com"
}
def launch_website(website_name):
    """
    Opens a website in the default browser.
    Returns True if successful, otherwise False.
    """

    website_name = website_name.lower()

    if website_name not in WEBSITES:
        return False

    try:
        webbrowser.open(WEBSITES[website_name])
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False