class GamerRating():
	def __init__(self, username, rating=0):
		self.name = username
		self.rating = rating
	
	def rating_increase(self,new_rating):
		self.rating += new_rating
	def rating_decrease(self,worse_rating):
		self.rating -= worse_rating

flag = "Apple"

while flag == "Apple":
	first_input = input("Please Enter A User Name:\n> ")
	second_input = input("Please Enter A Rating:\n> ")
	conversion = int(second_input)
	new_user = GamerRating(first_input, conversion)
	print("Your Chosen Username Is '{}'".format(new_user.name))
	print("Your Current Rating Is {}".format(new_user.rating))
	break_point = input("Enter 'Increase' or 'Decrease' to update your rating:\n> ")
	change = input("Enter the amount to change by:\n> ")
	number = int(change)
	if break_point == "Increase":
		new_user.rating_increase(number)
		print("Your new rating is {}".format(new_user.rating))
		flag = "Banana"
	elif break_point == "Decrease":
		new_user.rating_decrease(number)
		print("Your new rating is {}".format(new_user.rating))
		flag = "Banana"