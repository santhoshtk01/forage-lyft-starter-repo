from datetime import datetime, timedelta
from .battery_interface import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        """
        :param last_service_date : The date of the last service of the car. Format : mm/dd/yyyy.
        :param current_date : Current date from 'datetime.datetime'
        """
        self.last_service_date = last_service_date
        self.current_date = datetime.now()

    def needs_service(self) -> bool:
        """Checks the date and return `True` if car needs service. Otherwise, `False`."""
        next_service_date = datetime.strptime(self.last_service_date, '%m/%d/%Y') + timedelta(days=730)
        next_service_date = datetime(next_service_date.year, next_service_date.month, next_service_date.day)
        current_date = datetime(self.current_date.year, self.current_date.month, self.current_date.day)

        # Compare both dates to find if the car needs service or not.
        if current_date >= next_service_date:
            return True
        else:
            return False
