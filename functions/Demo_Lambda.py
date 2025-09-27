def increment(n):
    return n + 1


inc = increment

print(inc(20))

"""Lambda can accept all the different types of argument is an 
declarative type on programming 
syntax is :- variable_name  = lamdba <Params_list> : <Expression / condition>"""

l1 = lambda n: n + 1
print(l1(2))

l2 = lambda n1, n2, n3: n1 + n2 + n3
print(l2(1, 2, 3))

l3 = lambda n1, n2=9, n3=2: n1 + n2 + n3
print(l3(2, 3))

l4 = lambda *args: sum(args)
print(l4(1, 2, 3, 3, 4, 6, 4))

values = {'one': 1, 'two': 2, 'three': 3}
l5 = lambda **kwargs: sum((kwargs.values()))
print(l5(one=1, two=2, three=3))
print(l5(**values))
