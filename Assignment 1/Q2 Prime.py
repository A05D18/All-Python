""" 2. Find prime numbers between a given range - start(take start no) , end (take end number) """
num1 = int(input("Enter the lower limit: "))
num2 = int(input("Enter the upper limit: "))
arr = []

for i in range(num1,num2+1):
    if i > 1:
        isPrime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            arr.append(i)

print(f"The prime numbers between {num1} and {num2} are {arr}")



