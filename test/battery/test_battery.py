import unittest
from datetime import datetime
from battery import nubbin_battery, spindler_battery


class NubbinBatteryTest(unittest.TestCase):

    def test_battery_needs_service(self):
        current_date = datetime.now()
        last_serviced_date = '07/05/2003'

        nubbinBattery = nubbin_battery.NubbinBattery(last_serviced_date, current_date)
        self.assertTrue(nubbinBattery.needs_service())

    def test_battery_no_need_service(self):
        current_date = datetime.now()
        last_serviced_date = '06/12/2022'

        nubbinBattery = nubbin_battery.NubbinBattery(last_serviced_date, current_date)
        self.assertFalse(nubbinBattery.needs_service())


class SpindlerBatteryTest(unittest.TestCase):

    def test_battery_needs_service(self):
        current_date = datetime.now()
        last_serviced_date = '07/05/2003'

        spindlerBattery = spindler_battery.SpindlerBattery(last_serviced_date, current_date)
        self.assertTrue(spindlerBattery.needs_service())

    def test_battery_no_need_service(self):
        current_date = datetime.now()
        last_serviced_date = '06/12/2022'

        spindlerBattery = spindler_battery.SpindlerBattery(last_serviced_date, current_date)
        self.assertFalse(spindlerBattery.needs_service())


if __name__ == '__main__':
    unittest.main()