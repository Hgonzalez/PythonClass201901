word_list = []
word = input("Enter a word: ")
if word != "quit":
	word_list.append(word)
	
while word != "quit":
	word = input('Enter another word: ')
	if word != "quit" and word not in word_list:
		word_list.append(word)
		
for unique in word_list:
	print(unique) 