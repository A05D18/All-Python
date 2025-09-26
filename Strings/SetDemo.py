fruits = {"mango", "orange", "banana", "apple", "grapes"}
fruits1 = {"pear", "avocado", "mango"}
print(fruits)

print("mango" in fruits)
print("orange" not in fruits)

for i in fruits:
    print(i)

print("-------set methods--------------")
fruits.add("pineapple")
print(fruits)

fruits.remove("pineapple")  # error if item not present in set
fruits.discard("pineapple")  # no error if item not present in set
fruits.pop()  # randomly removes an item

fruits.update({"guava", "papaya"})
print(fruits)

print("-------set operations-----------")
union = fruits.union(fruits1)
union = fruits | fruits1  #same for above line just with operator
print(union)

print("----inter----")
inter = fruits & fruits1
print(inter)

sym_set = fruits.symmetric_difference(fruits1)
sym_set = fruits ^ fruits1  #same with operator
print(sym_set)  #other than common


polluted = {"delhi","gurgaon","mumbai","agra","jadugoda"}
populated = {"mumbai","pune","bangalore","chennai"}
print(populated - polluted)
print(polluted - populated)
print(polluted.intersection(populated))
print(polluted.symmetric_difference(populated))
print(polluted.union(populated))