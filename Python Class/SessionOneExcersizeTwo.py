sum_input = input("Please enter something to begin \n> ")

numb_count = 0
char_count = 0

for count in sum_input:
	if count.isdigit():
		numb_count += 1
	elif count.isalpha():
		char_count += 1
	else:
		print("%r contains a non-alphanumeric character, please try again." %sum_input)
print("There are %s letters." %char_count)
print("There are %s digits." %numb_count)