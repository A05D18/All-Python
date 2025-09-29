from VehiclePortal import Bike, Car, Vehicle
from Objects.Employees import Employee


class Policy:
    @staticmethod
    def display_policy(v: Vehicle, years):

        if years < 5:
            amount = v.calc_premium()
        else:
            amount = v.calc_premium() + 1000
        print(f"Total premium amount for {v} is: {amount}")

    print("----------user---------------")


class User:
    @staticmethod
    def show_premium(v: Vehicle):
        years = int(input("Enter how old is the vehicle: "))
        Policy.display_policy(v, years)


my_car = Car("Toyota", "Supra", 45000000, "Luxury")
my_bike = Bike("Ducati", "Paingale 1000", 3500000, "Sports")
# my_self = Employee(344,"bc",700 )
# User.show_premium(my_self)  # show the result and is duck typing

User.show_premium(my_car)
print("----------------------------------")
User.show_premium(my_bike)

print("-------admin--------")
# this is for admin
v = [my_car, my_bike]
for i in v:
    # print(Policy.display_policy(i,years=1))
    Policy.display_policy(i, years=1)
