import subprocess
APP_PATHS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe"
}
def launch_application(app_name):
    """
    Launches an application based on its name.
    Returns True if successful, otherwise False.
    """

    app_name = app_name.lower()

    if app_name not in APP_PATHS:
        return False

    try:
        subprocess.Popen(APP_PATHS[app_name])
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False