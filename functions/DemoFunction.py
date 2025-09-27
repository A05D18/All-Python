def simple_function():
    print("hello")


simple_function()


def addition(num1, num2):
    return num1 + num2


print(addition(12, 13))
result = addition([11, 12], [9, 8])
print(result)
result = addition((11, 12), (8, 4))
print(result)


def calc_discount(product, price):
    print(f"Discounted price for {product} is {price * 0.85}")


calc_discount("book", 400)  #positional arguments just pass values as the parameter list is
calc_discount(price=5000, product="sofa")  #Keyword arguments just give the arguments with their type


def calc_discount1(product="mac", price=130000):
    print(
        f"Discounted price for {product} is {price * 0.85}")  #default arguments if no args are provided these values will be taken


calc_discount1(price=320000)  #for specific args pass use keyword args

"""Variable arguments ----- function receive var args so any no of args can be provided
    Variable keyword arguments can also take list/tuple/dict as args"""


def add(*nums):
    total = 0
    for n in nums:
        total += n
    return total


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(add(*n1))

"""Var keyword args
when function receive var keyword args it can take any no of variables"""


def calc_avg(**kwargs):
    value = kwargs['values']
    total = 0
    for n in value:
        total += n
    print(total / len(value))


calc_avg(name='amar', values=[1, 2, 3, 4, 5, 6, 7, 8, 9])
