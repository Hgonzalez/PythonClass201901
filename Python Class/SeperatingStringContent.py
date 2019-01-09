string = "I have 5 apples"

string = string.split()

print(string)
print(type(string))

string2 = "I, have, 5, apples"

string2 = string2.split(",")

print(string2)
print(type(string2))

string3 = "I, have, 5, apples"

string3 = string3.split(",", 2)

print(string3)
print(type(string3))