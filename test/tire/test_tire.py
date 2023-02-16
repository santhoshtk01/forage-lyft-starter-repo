import unittest

from tire.carrigan import Carrigan
from tire.octoprime import Octoprime


class CarriganTireTest(unittest.TestCase):

    TEST_DATA_NO_NEED_SERVICE = [
        [0.1, 0.2, 0.3, 0],
        [0.8, 0.7, 0.6, 0.4],
        [0, 0.8, 0.1, 0.11]
    ]

    TEST_DATA_NEED_SERVICE = [
        [0.9, 1, 0.8, 0.1],
        [1, 0.1, 0.7, 0.9],
        [0.9, 0.9, 0.9, 0.9]
    ]

    def test_tire_needs_service(self):
        for data in self.TEST_DATA_NEED_SERVICE:
            carriganTire = Carrigan(data)
            self.assertTrue(carriganTire.needs_service())

    def test_tire_no_need_service(self):
        for data in self.TEST_DATA_NO_NEED_SERVICE:
            carriganTire = Carrigan(data)
            self.assertFalse(carriganTire.needs_service())


class OctoprimeTireTest(unittest.TestCase):

    TEST_DATA_NO_NEED_SERVICE = [
        [0.1, 0.2, 0.3, 0],
        [0.8, 0.7, 0.6, 0.4],
        [0, 0.8, 0.1, 0.11]
    ]

    TEST_DATA_NEED_SERVICE = [
        [0.9, 1, 0.8, 1],
        [1, 1, 0.7, 0.9],
        [0.9, 0.9, 0.9, 0.9]
    ]

    def test_tire_needs_service(self):
        for data in self.TEST_DATA_NEED_SERVICE:
            octoprimeTire = Octoprime(data)
            self.assertTrue(octoprimeTire.needs_service())

    def test_tire_no_need_service(self):
        for data in self.TEST_DATA_NO_NEED_SERVICE:
            octoprimeTire = Octoprime(data)
            self.assertFalse(octoprimeTire.needs_service())


if __name__ == '__main__':
    unittest.main()
