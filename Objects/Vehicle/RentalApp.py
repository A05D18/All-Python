from RentalService import Rental
from VehiclePortal import Taxi, Bus


class RentalApp:
    @staticmethod
    def display_rent(rental_vehicle: Rental):
        print("-----------Welcome to Rental App!-----------")
        hrs = int(input("Hours for which you want to rent: "))
        amount = rental_vehicle.calculate_rent(hrs)
        print(f"Total rent for {rental_vehicle}: Rs{amount}")


print("---THE USER---")
taxi = Taxi("Tata", "abc", 120000, 123)
RentalApp.display_rent(taxi)

taxi = Bus("Tata", "abc", 120000, 123)
RentalApp.display_rent(taxi)
