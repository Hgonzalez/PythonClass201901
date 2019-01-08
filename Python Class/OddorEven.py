number = input("Please enter a number: \n> ")

even_or_odd = int(number) % 2

if even_or_odd == 1:
	print("Entered number is odd.")
else:
	print("Entered number is even.")