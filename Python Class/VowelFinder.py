user_input = input("Enter something please: \n> ")

def vowel_finder(word):
	for a in range(len(word)):
		if word[a] in "aeiou":
			ind = a
			break
	return ind

find = vowel_finder(user_input)

print(find)		