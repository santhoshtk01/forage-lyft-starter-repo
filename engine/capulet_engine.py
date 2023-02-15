from .engine_interface import Engine


class CapuletEngine(Engine):
    """
    :param current_mileage : Current miles the car ran so far.
    :param last_service_mileage : At which miles the car was serviced lastly.
    """
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        """Check the mileage and return `True` if car needs service. Otherwise, `False`."""
        return self.current_mileage - self.last_service_mileage > 30000
