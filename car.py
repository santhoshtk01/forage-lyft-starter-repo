from battery.battery_interface import Battery
from engine.engine_interface import Engine
from serviceable import Serviceable
from tire.tire_interface import Tire


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service():
            return True
        else:
            return False
