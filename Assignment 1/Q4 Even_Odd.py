"""4. Count Digits, Even/Odd, Sum
e.g. 23456
output digits : 5
sum : 20
Even digits : 3
odd digits :2"""

num = int(input("Enter a number: "))
if num <= 0:
    print("Error: Enter a positive number")
    exit()
else:
    add = 0
    count = 0
    e_count = 0
    temp = num
    while num > 0:
        temp = num % 10
        add = add + temp
        num = num // 10
        if temp % 2 == 0:
            e_count += 1
        count += 1
    print(f"The sum of  digits are: {add}")
    print(f"The count of digits in number is: {count}")
    print(f"The even digits in number are: {e_count}")
    print(f"The odd digits in number are: {count-e_count}")





