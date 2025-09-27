import Maths
from Maths import subtraction as s
from Maths import division
n = int(input("enter 1 for add 2 for sub 3 for multi 4 for divi"))
n1 = int(input("enter first num"))
n2 = int(input("enter first num"))

match n:
    case 1:
        r = Maths.addition(n1,n2)
        print(r)
    case 2:
        r = s(n1,n2)
        print(r)
    case 3:
        r = Maths.multiplication(n1,n2)
        print(r)
    case 4:
        r = division(n1,n2)
        print(r)