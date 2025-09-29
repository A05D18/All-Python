from VehiclePortal import Vehicle, Bike, Car


v1 = Car("Toyota", "Supra", 45000000, "Luxury")
print("This is object of CAR:\n",v1)
print("-------------------------")

v2 = Bike("Ducati", "Paingale 1000", 3500000, "Sports")
print("This is object of Bike:\n",v2)

print("----------Premium Calculation-----------")

print(f"The premium of your {v1.model} is: ",v1.calc_premium())
print(f"The premium of your {v2.model} is: ",v2.calc_premium())
