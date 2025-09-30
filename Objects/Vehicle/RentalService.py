from abc import ABC, abstractmethod

class Rental(ABC):
    def __init__(self, rental_id):
        self.rental_id = rental_id

    @abstractmethod
    def calculate_rent(self,hrs):
        pass

    def __str__(self):
        return f" Rental id: {self.rental_id}"


