from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    @abstractmethod
    def calc_premium(self):
        pass  #to define abstract method in superclass

    def __str__(self):
        return f"The make is: {self.make}\n model is: {self.model}\n price is: {self.price}\n"


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
        return super().__str__() + f" The Segment is: {self.segment}"


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
