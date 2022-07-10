class Tires:

    def __init__(self):
        pass

    def needs_service(self):
        pass


class CarriganTires(Tires):
    # Carrigan tires should be serviced only
    # when one or more of the values in the tire wear array is greater than or equal to 0.9.
    def __init__(self, tire_wear):
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self):
        for tire in self.tire_wear:
            if tire >= 1.0:
                result = True
                break
            else:
                result = False
        return result


class OctoprimeTires(Tires):
    # Octoprime tires should be serviced only
    # when the sum of all values in the tire wear array is greater than or equal to 3
    def __init__(self):
        super().__init__()

    def needs_service(self):
        return True

