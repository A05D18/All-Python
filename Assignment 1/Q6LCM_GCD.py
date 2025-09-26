"""6. Find LCM and GCD for given numbers [take 2 numbers] using loops only"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 <= 0 or num2 <= 0:
    print("Error: Enter Positive numbers.")
else:
    a = num1
    b = num2
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
        gcd = num2
    lcm = (a * b)// gcd
    print(f"The GCD of {a} & {b} is: {gcd}")
    print(f"The LCM of {a} & {b} is: {lcm}")
