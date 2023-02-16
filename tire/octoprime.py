from .tire_interface import Tire


class Octoprime(Tire):

    def __init__(self, tire_sensor_data: list):
        self.tire_sensor_data = tire_sensor_data

    def needs_service(self) -> bool:
        if int(sum(self.tire_sensor_data)) >= 3:
            return True
        else:
            return False

