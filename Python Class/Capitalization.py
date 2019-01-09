user_input = input("Enter a word to begin, to quit type 'quit': \n> ")

def character(x):
	chars = ("?",".","!")
	if x in chars:
		return True
	else:
		return False

def character_replace(x):
	word = " "
	for i in range(len(x)-2):
		if character(x[i]):
			#print("hgjhhj",x[i],i)
			newindex = i+2 
			#print("nnnn",newindex)
			first_letter = x[newindex].upper()
			#print(capital_letter) 
			#print(replaced_string[0:newindex])
			#print(replaced_string[newindex+1:])
			word = replaced_string[0:newindex]+ first_letter + replaced_string[newindex+1:]
			#print ("KKK",word)

#		else:
#			newindex = i+2
#			capital_letter = x[newindex].capitalize() 
#			word = replaced_string[0:newindex]+ capital_letter + replaced_string[newindex+1:]
	print (word)

replaced_string = user_input.replace(" i ", " I ")
replaced_string = replaced_string.capitalize()

character_replace(user_input)