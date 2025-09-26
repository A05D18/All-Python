"""Q.4. Write a Python program to remove duplicates from a list"""

l1 = [1,2,3,4,5,6,7,2,3,1,6,9,9,8]
st = set(l1)
l1 = list(st)
print(l1)