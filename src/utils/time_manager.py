from datetime import datetime

class TimeManager:
    """
    Handles all date and time related operations.
    """

    def get_current_time(self):
        """
        Returns the current time.
        """

        current_time = datetime.now()

        return current_time.strftime("%I:%M %p")
    
    def get_current_date(self):
        """
        Returns the current date.
        """

        current_date = datetime.now()

        return current_date.strftime("%d %B %Y")
    
    def get_current_day(self):
        """
        Returns the current day of the week.
        """

        current_day = datetime.now()

        return current_day.strftime("%A")