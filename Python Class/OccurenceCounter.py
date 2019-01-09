word = input("Enter something:\n> ")

lower_word = str(word.lower())

d ={}

for char in lower_word:
	if char not in d:
		d[char] = 1
	else:
		d[char] = d[char] + 1
		
print(d)