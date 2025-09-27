def infinite_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, b + a


def print_infi_fib(n):
    fib_gen = infinite_fib()
    # for i in range(n):
    #     print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))
    print(next(fib_gen))


print_infi_fib(50)
