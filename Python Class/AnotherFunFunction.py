def math(a,b):
	summary = ("Your total is {}".format(a + b))
	product = ("Your product is {}".format(a * b))
	return summary,product
number_one = int(input("enter a number:\n> "))
number_two = int(input("enter a second number:\n "))
x,y = math(number_one,number_two)
print(x)
print(y)