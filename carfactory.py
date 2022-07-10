from datetime import date
from components.battery import SpindlerBattery, NubbinBattery
from components.engine import WilloughbyEngine, CapuletEngine, SternmanEngine
from components.tires import CarriganTires, OctoprimeTires
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
                        last_service_mileage: int,
                        tire_wear_status) -> Car:

        self.engine = CapuletEngine(last_service_mileage, current_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.tires = CarriganTires(tire_wear_status)
        return Car(self.engine, self.battery, self.tires)

    def create_glissade(self,
                            current_date: date,
                            last_service_date: date,
                            current_mileage: int,
                            last_service_mileage: int,
                            tire_wear_status) -> Car:
        self.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        self.tires = OctoprimeTires(tire_wear_status)
        return Car(self.engine, self.battery, self.tires)

    def create_palindrome(self,
                            current_date: date,
                            last_service_date: date,
                            warning_light_on: bool,
                            tire_wear_status) -> Car:
        self.engine = SternmanEngine(warning_light_on)
        self.battery = NubbinBattery(last_service_date, current_date)
        self.tires = CarriganTires(tire_wear_status)
        return Car(self.engine, self.battery, self.tires)

    def create_rorschach(self,
                            current_date: date,
                            last_service_date: date,
                            current_mileage: int,
                            last_service_mileage: int,
                            tire_wear_status) -> Car:
        self.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.battery = NubbinBattery(last_service_date, current_date)
        self.tires = OctoprimeTires(tire_wear_status)
        return Car(self.engine, self.battery, self.tires)

    def create_thovex(self,
                            current_date: date,
                            last_service_date: date,
                            current_mileage: int,
                            last_service_mileage: int,
                            tire_wear_status) -> Car:
        self.engine = CapuletEngine(last_service_mileage, current_mileage)
        self.battery = NubbinBattery(last_service_date, current_date)
        self.tires = CarriganTires(tire_wear_status)
        return Car(self.engine, self.battery, self.tires)
