cards = ("spade","heart","club","spade")
print(cards)

print("spade" in cards)
print("heart" not in cards)

for item in cards:
    print(item)

print('-------------------------------------------')
one, two, three, four = cards #tuple unpacking
print(three)

print('-------------------------------------------')
l_cards = list(cards)
l_cards.append("random")
cards = tuple(l_cards)
print(cards)

print('-------------------------------------------')
t1 = (1,2,3,4,5,6)
t2 = ("one","two","three","four")
t1, t2 = t2, t1
print(t1)
print(t2)

t3 = tuple(zip(t1,t2))
print(t3)

print(cards[::-1]) #reverse order print
print(cards[0:3])