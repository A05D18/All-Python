"""Q.3.  Write a Python function that takes a list of words and returns the length of the longest one"""

num = int(input("Enter no. of words u want to add in string: "))
List1 = []
for i in range(num):
    str1 = input("Enter the word: ")
    List1.append(str1)
print(List1)

longest = ''

for j in range(len(List1)):
    if len(List1[j]) > len(longest):
        longest = List1[j]
print(longest)
