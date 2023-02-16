import unittest
from datetime import datetime
from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, sternman_engine, willoughby_engine


class NubbinBatteryTest(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        current_date = datetime.now()
        last_serviced_date = '07/05/2003'

        nubbinBattery = nubbin_battery.NubbinBattery(last_serviced_date, current_date)
        self.assertTrue(nubbinBattery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.now()
        last_serviced_date = '06/12/2022'

        nubbinBattery = nubbin_battery.NubbinBattery(last_serviced_date, current_date)
        self.assertFalse(nubbinBattery.needs_service())


class SpindlerBatteryTest(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        current_date = datetime.now()
        last_serviced_date = '07/05/2003'

        spindlerBattery = spindler_battery.SpindlerBattery(last_serviced_date, current_date)
        self.assertTrue(spindlerBattery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.now()
        last_serviced_date = '06/12/2022'

        spindlerBattery = spindler_battery.SpindlerBattery(last_serviced_date, current_date)
        self.assertFalse(spindlerBattery.needs_service())


class CapuletEngineTest(unittest.TestCase):

    def test_engine_needs_service(self):
        current_miles = 50000
        last_serviced_miles = 19000

        capuletEngine = capulet_engine.CapuletEngine(current_miles, last_serviced_miles)
        self.assertTrue(capuletEngine.needs_service())

    def test_engine_no_need_service(self):
        current_miles = 50000
        last_serviced_miles = 30000

        capuletEngine = capulet_engine.CapuletEngine(current_miles, last_serviced_miles)
        self.assertFalse(capuletEngine.needs_service())


class StrenmanEngineTest(unittest.TestCase):

    def test_engine_needs_service(self):
        warning_light = True

        sternmanEngine = sternman_engine.SternmanEngine(warning_light)
        self.assertTrue(sternmanEngine.needs_service())

    def test_engine_no_need_service(self):
        warning_light = False

        sternmanEngine = sternman_engine.SternmanEngine(warning_light)
        self.assertFalse(sternmanEngine.needs_service())


class WilloughbyEngineTest(unittest.TestCase):

    def test_engine_needs_service(self):
        current_miles = 86000
        last_serviced_miles = 25000

        willoughbyEngine = willoughby_engine.WilloughbyEngine(current_miles, last_serviced_miles)
        self.assertTrue(willoughbyEngine.needs_service())

    def test_engine_no_need_service(self):
        current_miles = 86000
        last_serviced_miles = 26000

        willoughbyEngine = willoughby_engine.WilloughbyEngine(current_miles, last_serviced_miles)
        self.assertFalse(willoughbyEngine.needs_service())


if __name__ == '__main__':
    unittest.main()
