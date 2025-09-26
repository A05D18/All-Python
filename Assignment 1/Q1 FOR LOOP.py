""""1. Using for loop, write and run a Python program for this algorithm.
Here is an algorithm to print out n! from 0! to 10! """

num = int(input("Enter a number from 0 to 10: "))
print(num)
temp = num

if num == 0:
    print(0)
elif num == 1:
    print(1)
else:
    for i in range(1, num):
        num = num * i

print(f"The Factorial is {temp} is {num} ")
