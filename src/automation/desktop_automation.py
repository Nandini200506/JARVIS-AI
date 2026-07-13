import os
import pyautogui

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

    def volume_up(self):
        """
        Increase the system volume.
        """

        pyautogui.press("volumeup")

    def volume_down(self):
        """
        Decrease the system volume.
        """

        pyautogui.press("volumedown")

    def mute_volume(self):
        """
        Toggle the system mute state.
        """

        pyautogui.press("volumemute")