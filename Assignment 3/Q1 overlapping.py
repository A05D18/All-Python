l1 = [1, 2, 3 ]
l2 = [4, 5, 6, 7, 8, 9]


def overlapping(lis1, lis2):
    lis1 = set(lis1)
    lis2 = set(lis2)
    res = False
    if lis1.intersection(lis2):
        res = True
    if res:
        print("There is at least one element common")
    else:
        print("There's nothing in common")


overlapping(l1, l2)
