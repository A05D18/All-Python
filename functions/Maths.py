def addition(num1, num2):
    return num1 + num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def subtraction(num1, num2):
    return num1 - num2

if __name__ == "__main__":
    print("Functions calling by passing args: "
          "\n Addition is: ", addition(4, 5),
          "\n Subtraction is: ", subtraction(4, 3),
          "\n Multiplication is: ", multiplication(5, 6),
          "\n Division is: ", division(10, 5)
          )

