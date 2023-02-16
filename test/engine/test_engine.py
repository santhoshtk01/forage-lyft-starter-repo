import unittest
from engine import capulet_engine, sternman_engine, willoughby_engine




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
