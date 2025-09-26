"""5. Write a program to check if given triangle is valid if 3 sides of the triangle are provided.
Also print the type of triangle"""
side1 = int(input("Enter first side of the triangle: "))
side2 = int(input("Enter second side of the triangle: "))
side3 = int(input("Enter third side of the triangle: "))
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Error: Please enter all valid sides of the triangle")
elif side1 + side2 < side3 or side2 + side3 < side1 or side3 + side1 < side2:
    print("Error: Not a valid Triangle")
else:
    if side1 == side2 == side3:
        print("The given triangle is Equilateral Triangle.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The given triangle is Isosceles Triangle.")
    elif side1 ** 2 + side2 ** 2 == side3**2 or side2 ** 2 + side3 ** 2 == side1**2 or side1 ** 2 + side3 ** 2 == side2**2 :
        print("The given triangle is Right Angled Triangle.")
    else:
        print("The given triangle is Scalene Triangle.")
