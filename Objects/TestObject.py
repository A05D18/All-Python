from Employees import Employee, NewEmployee

from datetime import date

e1 = Employee()  # __init__ with default parameter
print(e1)
print(repr(e1))
"""str vs repr
__str__ gives informal representation of an object often used for printing
__repr__ gives formal representation of an object often used for reconstruction"""

print("__________")
e2 = eval(repr(e1))
print(e2)
print(type(e2))

print(e1.calculate_sal())

e3 = Employee(101, "Amar", 5000000)
print(e3)
print(repr(e3))

print(e3.calculate_sal())

e4 = NewEmployee("Amar", 50000)
e5 = NewEmployee(name="DJ")
print(repr(e4))

# print(e4.__repr__(), "This is repr 2")

NewEmployee.show_employee_count()
NewEmployee.set_count()
e6 = NewEmployee()
NewEmployee.show_employee_count()
