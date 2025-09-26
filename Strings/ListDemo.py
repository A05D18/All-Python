words = ["pat","bat","mat","rat","sat","fat","sat"]
print(words)

for items in words:
    print(items)

print("fat" in words)
print("fit" not in words)

print(words[5])
print(words[-5])
#print(words[10])
print(words[1:6])
print(words[-6:-1])
print(words[-6:-1:-1])
print(words[-1:-6:-1])
print(words[::-1])
print(words[:4] + words[4:])

print("-------------List methods------------")
words.append("mat")
print(words)
print("-----remove-------")
#if try to remove item which is not present throws error
words.remove("mat")
print(words)
print("------append list in list---------")
words.append(["sat","cat"])
print(words)
print("-------append words in list------------")
words.extend(["sat","cat"])
print(words)
print("-----pop-----")
words.pop(3)
print(words)
print("------insert at index 3--------")
words.insert(3, "dat")
print(words)
print("reverse---------")
words.reverse()
print(words)
count = [words.count(word) for word in words]
print(count)
print(sum(count))


print("\n\n changing the list value using expressions and storing it as list")
nums = [2 ,3 ,4 ,5]
sq = [i*i for i in nums]
print(sq)


