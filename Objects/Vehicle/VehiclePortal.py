from abc import ABC, abstractmethod

from Objects.Vehicle.RentalService import Rental


class Vehicle(ABC):
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    @abstractmethod
    def calc_premium(self):
        pass  # to define abstract method in superclass

    def __str__(self):
        return f" Make: {self.make}\n Model: {self.model}\n Price: {self.price}\n"


class Car(Vehicle):
    def __init__(self, make, model, price, segment="Standard"):
        super().__init__(make, model, price)
        self.segment = segment

    def calc_premium(self):

        if self.segment == 'Luxury':
            return self.price * 0.025
        else:
            return self.price * 0.01

    def __str__(self):
        return super().__str__() + f" The Segment: {self.segment}\n"


class Bike(Vehicle):

    def __init__(self, make, model, price, segment="Standard"):
        super().__init__(make, model, price)
        self.segment = segment

    def calc_premium(self):
        if self.segment == "Sports":
            return self.price * 0.02
        else:
            return self.price * 0.01

    def __str__(self):
        return super().__str__() + f" The segment is: {self.segment}"


class Taxi(Car, Rental):
    def __init__(self, make, model, price, rental_id, segment='Standard'):
        Car.__init__(self, make, model, price, segment)
        Rental.__init__(self, rental_id)

    def calculate_rent(self, hrs):
        if hrs <= 8:
            return hrs * 250
        else:
            return hrs * 250 + (hrs - 8) * 200

    def __str__(self):
        return Car.__str__(self) + Rental.__str__(self)


class Bus(Vehicle, Rental, ABC):
    def __init__(self, make, model, price, rental_id, ):
        Vehicle.__init__(self, make, model, price)
        Rental.__init__(self, rental_id)

    def calculate_rent(self, hrs):
        if hrs <= 8:
            return hrs * 1000
        else:
            return hrs * 1000 + (hrs - 8) * 200

    def calc_premium(self):
        return self.price * 0.03

    def __str__(self):
        return Vehicle.__str__(self) + Rental.__str__(self)


taxi = Taxi("Suzuki", "Waganor", 200000, 9211)
print(taxi)
print(f"{taxi.calculate_rent(5)} , {taxi.rental_id}")

bus = Bus("Tata", "35 Seater", 1200000, 9211)
print(bus)
print(bus.calculate_rent(5))
print(bus.calc_premium())
