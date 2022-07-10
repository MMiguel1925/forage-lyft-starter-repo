from serviceable import Serviceable


class Car(Serviceable):
    """
    Represents a Car with a composition of diferent parts of a car.
    """
    def __init__(self, engine, battery, tires):
        super().__init__()
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        """
        Verify if the car components needs service, and returns true if any of them return true
        :return: True or False
        """
        if self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service():
            return True
        else:
            return False
