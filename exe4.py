class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_info(self):
        return f"Car - {super().display_info()}, Fuel Type: {self.fuel_type}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model, "Electric")
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"Electric Car - {super().display_info()}, Battery Capacity: {self.battery_capacity} kWh"


class Bicycle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def display_info(self):
        return f"Bicycle - {super().display_info()}, Type: {self.type}"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_type):
        super().__init__(brand, model)
        self.engine_type = engine_type

    def display_info(self):
        return f"Motorcycle - {super().display_info()}, Engine Type: {self.engine_type}"



vehicle = Vehicle("Generic Brand", "Generic Model")
print(vehicle.display_info())

car = Car("Toyota", "Camry", "Petrol")
print(car.display_info())

electric_car = ElectricCar("Tesla", "Model S", 75)
print(electric_car.display_info())

bicycle = Bicycle("Giant", "Escape", "Mountain")
print(bicycle.display_info())

motorcycle = Motorcycle("Honda", "CBR500R", "Inline-4")
print(motorcycle.display_info())
