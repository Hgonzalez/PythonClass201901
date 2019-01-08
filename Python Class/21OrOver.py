customer_age = input("What is your current age? \n> ")

if customer_age.isdigit() is True:
	customer_age = int(customer_age)
	if customer_age > 21:
		print("You are %s years old, you are older than 21." %customer_age)
	elif customer_age < 21:
		print("You are %s years old, you are not older than 21, please leave." %customer_age)
	elif customer_age == 21:
		print("You are %s years old, you are exactly 21." %customer_age)
else:
	print("%r is not a valid number, please try again." %customer_age)