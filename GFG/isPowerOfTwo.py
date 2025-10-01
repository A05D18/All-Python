"""Given a non-negative integer n. You have to check if it is a power of 2 or not. """


import math


def isPowerOfTwo(n):
    if n <= 0:
        return False
    # Check if log2(n) is an integer
    log_val = math.log2(n)
    return log_val.is_integer()
    # return (n & (n - 1)) == 0


# Read input and print output
n = int(input("enter no: "))
print(isPowerOfTwo(n))
