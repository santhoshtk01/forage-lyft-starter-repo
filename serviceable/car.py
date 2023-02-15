from battery.main import Battery
from engine.main import Engine


class Car:
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        """
        Implement this method so that it return weather the car needs service or not
        based on the `Engine` and `Battery` object.
        """
        pass
