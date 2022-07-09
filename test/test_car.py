import unittest
from datetime import datetime
from components.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from components.battery import SpindlerBattery, NubbinBattery


class TestEngine(unittest.TestCase):

    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        self.assertTrue(CapuletEngine(last_service_mileage, current_mileage).needs_service(),
                        'Expected result = True')

    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        self.assertFalse(CapuletEngine(last_service_mileage, current_mileage).needs_service(),
                         'Expected result = False')

    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        self.assertTrue(WilloughbyEngine(last_service_mileage, current_mileage).needs_service(),
                        'Expected result = True')

    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        self.assertFalse(WilloughbyEngine(last_service_mileage, current_mileage).needs_service(),
                         'Expected result = False')

    def test_sternman_engine_should_be_serviced(self):
        warning_light_on = True
        self.assertTrue(SternmanEngine(warning_light_on).needs_service(),
                        'Expected result = True')

    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_on = False
        self.assertFalse(SternmanEngine(warning_light_on).needs_service(),
                         'Expected result = False')


class TestBattery(unittest.TestCase):

    def test_spindler_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        self.assertTrue(SpindlerBattery(last_service_date, current_date).needs_service(),'Expected result = True')

    def test_spindler_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        self.assertFalse(SpindlerBattery(last_service_date, current_date).needs_service(),'Expected result = False')

    def test_nubbin_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        self.assertTrue(NubbinBattery(last_service_date, current_date).needs_service(),'Expected result = True')

    def test_nubbin_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        self.assertFalse(NubbinBattery(last_service_date, current_date).needs_service(),'Expected result = False')


if __name__ == '__main__':
    unittest.main(verbosity=2)
