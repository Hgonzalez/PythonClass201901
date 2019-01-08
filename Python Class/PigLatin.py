word = input("Enter a word \n> ")


if word[0] in "aeiou":
	result = (word + "y")
	print(result)
else:
	for a in range(len(word)):
		print(a, word[a])
		if word[a] in "aeiou":
			x = a
			first = word[0:x]
			second = word[x:]
			whole = second + first + "ay"
			break
print(whole)