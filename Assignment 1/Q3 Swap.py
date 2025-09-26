"""3. Write a python program to swap a 3 digit number
input 321
output 123"""

num = int(input("Enter a three digit number: "))
temp = num
reversed_num = 0
while num > 0:
    temp = num % 10
    reversed_num = reversed_num * 10 + temp
    num = num // 10
print(f"Reversed number is: {reversed_num}")



