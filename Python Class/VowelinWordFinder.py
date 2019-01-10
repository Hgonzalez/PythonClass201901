user_input = input("Enter a letter \n> ")

def is_vowel(x):
	vowel_finder = []
	if x in "aeiou":
		vowel_finder.append(x)		
		vowel_finder.append(True)
	else:
		vowel_finder.append(x)
		vowel_finder.append(False)
	return(vowel_finder)

whatami = [is_vowel(char) for char in user_input] 
print(whatami)

user_input = input("Enter a letter \n> ")

def is_vowel(x):
	vowel_finder = []
	if x in "aeiou":
		vowel_finder.append(x)		
		return x,True
	else:
		vowel_finder.append(x)
		return x,False
	return(vowel_finder)

whatami = [is_vowel(char) for char in user_input] 
print(whatami)