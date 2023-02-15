from main import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = None

    def needs_service(self) -> bool:
        # TODO: Should be serviced every two 2 years.
        pass
