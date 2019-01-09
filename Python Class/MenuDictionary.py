meals = {'Hamburger': 8, 'Bacon Burger': 8.50, 'Hot Dogs': 2}
print("These are the meals on our menu", meals)
drinks = {'Soda': 2, 'Beer': 7, 'Juice': 2}
print("These are the drinks on our menu", drinks)

menu = {}
menu.update(meals)
menu.update(drinks)
print(menu)

user_input = input("Enter the meal you would like: \n> ")

meal_total = 0

drink_total = 0

for item in user_input:
	if item in meals:
		print(item)
		meal_total.sum(item)
	elif item in drinks:
		print(item)
		drink_total
	else:
		print("You did not enter an item on the menu")

print("Your total is:\n", meal_total + drink_total)