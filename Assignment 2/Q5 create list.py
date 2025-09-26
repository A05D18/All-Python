"""Q 5. Create a list of books
e.g. booklist =[['Java 8', 700], ['Python for Beginners', 500],....]

Perform following operations on the list
1. Add a new book with price
2. Remove entry for a book
3. update price for a book
4. Sort the list by book names
5. Sort the list by prices
6. Print the book with max and min price [hint : you may use min()/max() functions of python]"""
from operator import itemgetter

booklist = [['Java 8', 700], ['Python for Beginners', 500], ['Data Structures with Python', 600],
            ['C++ Programming', 800], ['Machine Learning Basics', 900], ['Web Development with Django', 550]]
# 1. Add a new book with price
booklist.append(['Linux learning', 900])
# 2. Remove entry for a book
booklist.remove(['Java 8', 700])
# 3. update price for a book
booklist[0][1] = 500
# 4. Sort the list by book names
print("---Sorted By Book Name-----")
booklist.sort(key=itemgetter(0))
for i in range(len(booklist)):
    print(booklist[i])
# 5. Sort the list by prices
print("---Sorted By Book Price-----")
booklist.sort(key=itemgetter(1))
for i in range(len(booklist)):
    print(booklist[i])
# 6. Print the book with max and min price

print("-----------------------")
print(max(booklist, key=itemgetter(1)))

# Min Price

print("-----------------------")
print(min(booklist, key=itemgetter(1)))

print("-----------------------")
