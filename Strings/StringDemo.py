s = "Python is a dynamic language"
is_present = 'Python' in s
print(is_present)

not_present = 'Java' not in s
print(not_present)

print("------------------------")
print(s[8])
print(s[-8])
print(s[3:10])
print(s[-10:-3])
#print(s[40])   IndexError: string index out of bound
print(s[2:14:2])
print(s[::-1])
'''for third negative,start index should be greater than end index and it reverse the string if no value
is given it takes the entire string'''
print(s[:10] + s[10:])

print("-----------char classification--------------------------")
s1 = "hello"
print(s1.isalpha())
print(s1.isidentifier())
s1 = "1234"
print(s1.isdecimal())
s1 = "12\u00B2"
print(s1.isdigit())
s1 = "12\u00B2\u2168"
print(s1.isnumeric())
print(s1.isalnum())
print(s1.isprintable())
print(s1.isidentifier())

print("--------------char conversion----------------------")
s2 = "welcome TO python"
print(s2.lower())
print(s2.upper())
print(s2.title())
print(s2.capitalize())
print(s2.count("o"))
print(s2.find("o"))
print(s2.swapcase())


print("----------------other method----------------------------")
s3 = "sit bit        fit dont but do it "
s3 = s3.strip()
print(s3)
words = s3.split(" ")
print(words)
partition = s3.partition("bit")
print(partition)