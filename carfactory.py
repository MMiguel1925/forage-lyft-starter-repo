from datetime import date
from components.battery import SpindlerBattery, NubbinBattery
from components.engine import WilloughbyEngine, CapuletEngine, SternmanEngine
from car import Car


class CarFactory:
    """
    The CarFactory class declares the create method's to return an
    object of a Car class.
    """
    def __init__(self):
        pass

    def create_calliope(self,
                        current_date: date,
                        last_service_date: date,
                        current_mileage: int,
                        last_service_mileage: int) -> Car:
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.engine = CapuletEngine(self.last_service_mileage, self.current_mileage)
        self.battery = SpindlerBattery(self.last_service_date, self.current_date)
        return Car(self.engine, self.battery)

    def create_glissade(self,
                            current_date: date,
                            last_service_date: date,
                            current_mileage: int,
                            last_service_mileage: int) -> Car:
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.engine = WilloughbyEngine(self.last_service_mileage, self.current_mileage)
        self.battery = SpindlerBattery(self.last_service_date, self.current_date)
        return Car(self.engine, self.battery)

    def create_palindrome(self,
                            current_date: date,
                            last_service_date: date,
                            warning_light_on: bool):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.warning_light_on = warning_light_on
        self.engine = SternmanEngine(self.warning_light_on)
        self.battery = NubbinBattery(self.last_service_date, self.current_date)
        return Car(self.engine, self.battery)

    def create_rorschach(self,
                            current_date: date,
                            last_service_date: date,
                            current_mileage: int,
                            last_service_mileage: int):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.engine = WilloughbyEngine(self.last_service_mileage, self.current_mileage)
        self.battery = NubbinBattery(self.last_service_date, self.current_date)
        return Car(self.engine, self.battery)

    def create_thovex(self,
                            current_date: date,
                            last_service_date: date,
                            current_mileage: int,
                            last_service_mileage: int):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.engine = CapuletEngine(self.last_service_mileage, self.current_mileage)
        self.battery = NubbinBattery(self.last_service_date, self.current_date)
        return Car(self.engine, self.battery)
