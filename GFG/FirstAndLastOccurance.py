"""Given a sorted array arr with possibly some duplicates, the task is to find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1."""


def findFirstAndLast(arr, x):
    first = last = -1
    for i in range(len(arr)):
        if arr[i] == x:
            if first == -1:
                first = i
            last = i
    return [first, last]


arr1 = [1, 2, 4, 6, 7, 3, 5, 7, 6, 52, 7, 8, 5, 4, 3, 5, 6, 7, 7, 8, 8, 3, 5]
print(findFirstAndLast(arr1, 7))
