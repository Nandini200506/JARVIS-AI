import os


class DesktopAutomation:
    """
    Handles all desktop automation tasks.
    """

    def open_notepad(self):
        """
        Open Windows Notepad.
        """
        os.system("start notepad")

    def open_calculator(self):
        """
        Open Windows Calculator.
        """
        os.system("start calc")