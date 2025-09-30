import sys

try:
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))

    result = dividend / divisor

    print(result)
except ZeroDivisionError as e:
    print(e)
    e_type, e_cause, e_trace = sys.exc_info()
    print(f"{e_type}, {e_cause}, {e_trace}")
    print(f'{e.with_traceback(None)}')

except ValueError as e:
    print(e)
