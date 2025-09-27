from functools import reduce

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def calc_square(n):
    return n * n


sq = list(map(calc_square, num))
print(sq)

sq2 = list(map(lambda item: item * item, num))
print(sq2)

sq3 = list(filter(lambda n: n % 2 == 0, num))
print(sq3)

min_num = reduce(lambda n, n2: n if n < n2 else n2, num)
print(min_num)

max_num = reduce(lambda n, n2: n if n > n2 else n2, num)
print(max_num)

filtered = list(filter(lambda item: item > 10, num))
print(filtered)