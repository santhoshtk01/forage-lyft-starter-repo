from .tire_interface import Tire


class Carrigan(Tire):

    def __init__(self, tire_sensor_data: list):
        self.tire_sensor_data = tire_sensor_data

    def needs_service(self) -> bool:
        for value in self.tire_sensor_data:
            if value >= 0.9:
                return True
        return False
