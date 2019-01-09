first_input = int(input("Enter one number:\n> "))
second_input = int(input("Enter second number:\n> "))
#user_input = user_input.split()
#user_input = int(user_input)

def add(x,y):
	total = x + y
	return total
print(add(first_input,second_input))

answer = lambda x,y : x+y
print(answer(first_input,second_input))