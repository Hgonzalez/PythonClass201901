user_input = input("Enter a letter \n> ")

def is_vowel(x):
	if x in "aeiou":		
		y = "{} is a vowel.".format(x)
	else:
		y = "{} is not a vowel.".format(x)
	return(y)
	
print(is_vowel(user_input))