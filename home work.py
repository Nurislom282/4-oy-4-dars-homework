from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, model, year, mileage, num_doors):
        super().__init__(brand, model, year, mileage)
        self.num_doors = num_doors

    def get_info(self):
        return f"Car: {self.brand} {self.model}, Year: {self.year}, Mileage: {self.mileage}, Doors: {self.num_doors}"

    def start(self):
        return "Car is starting."

    def stop(self):
        return "Car is stopping."

    def open_trunk(self):
        return "Trunk is open."

class Bicycle(Vehicle):
    def __init__(self, brand, model, year, mileage, gear_count):
        super().__init__(brand, model, year, mileage)
        self.gear_count = gear_count

    def get_info(self):
        return f"Bicycle: {self.brand} {self.model}, Year: {self.year}, Mileage: {self.mileage}, Gears: {self.gear_count}"

    def start(self):
        return "Bicycle ride started."

    def stop(self):
        return "Bicycle ride stopped."

    def ring_bell(self):
        return "Ring ring!"

car = Car("Toyota", "Corolla", 2020, 15000, 4)
bicycle = Bicycle("Giant", "Escape 3", 2021, 500, 21)

print(car.get_info())
print(car.start())
print(car.open_trunk())
print(car.stop())

print(bicycle.get_info())
print(bicycle.start())
print(bicycle.ring_bell())
print(bicycle.stop())
