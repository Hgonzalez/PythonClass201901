user_input = " "

while user_input != "quit":
	user_input = input("Enter a word to begin, to quit type 'quit': \n> ")
	user_input = user_input.lower()
	user_input = user_input.replace(" ",user_input)
	x = []
	x = x.append(user_input)
print(x)