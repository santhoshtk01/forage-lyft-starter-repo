from car import Car
from datetime import datetime

# Engines
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

# Batteries
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

# Tire
from tire.carrigan import Carrigan
from tire.octoprime import Octoprime

class CarFactory:

    def create_calliope(self, current_date, last_service_date,
                        current_mileage: int, last_service_mileage: int,
                        tire_sensor_data: list) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = Carrigan(tire_sensor_data)

        return Car(engine, battery, tire)

    def create_glissade(self, current_date, last_service_date,
                        current_mileage: int, last_service_mileage: int,
                        tire_sensor_date: list) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = Carrigan(tire_sensor_date)

        return Car(engine, battery, tire)

    def create_palindrom(self, current_date, last_service_date,
                         warning_light_on: bool, tire_sensor_data: list) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = Octoprime(tire_sensor_data)

        return Car(engine, battery, tire)

    def create_rorschach(self, current_date, last_service_date,
                         current_mileage: int, last_service_milage: int,
                         tire_sensor_data: list) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_milage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = Octoprime(tire_sensor_data)

        return Car(engine, battery, tire)

    def create_thovex(self, current_date, last_service_date,
                      current_mileage: int, last_service_mileage: int,
                      tire_sensor_data: list) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = Carrigan(tire_sensor_data)

        return Car(engine, battery, tire)


if __name__ == '__main__':
    pass
