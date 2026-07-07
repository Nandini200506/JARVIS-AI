import os
from pathlib import Path
FOLDERS = {
    "desktop": Path.home() / "Desktop",
    "downloads": Path.home() / "Downloads",
    "documents": Path.home() / "Documents",
    "pictures": Path.home() / "Pictures",
    "music": Path.home() / "Music",
    "videos": Path.home() / "Videos"
}
def open_folder(folder_name):
    """
    Opens a folder from the predefined FOLDERS dictionary.
    Returns True if successful, otherwise False.
    """

    folder_name = folder_name.lower()

    if folder_name not in FOLDERS:
        return False

    try:
        os.startfile(FOLDERS[folder_name])
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False