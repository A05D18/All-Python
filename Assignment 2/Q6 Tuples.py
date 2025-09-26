"""Q.6. Write a Python program to compute element-wise sum of given tuples, using “zip()” function
Original tuples:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6)"""
tup1 = (1,2,3,4)
tup2 = (3,5,2,1)
tup3 = (2,2,3,1)

tup4 = tuple(sum(elements) for elements in zip(tup1, tup2, tup3))
print(f"Element-wise sum of the said tuples: {tup4}")
