word = input("Enter the first possible anagrams:\n> ")
lower_word1 = str(word.lower())
word1a = {}
word2 = input("Enter the second possible anagrams:\n> ")
lower_word2 = str(word2.lower())
words = lower_word1 + lower_word2

for char in words:
	#print(words)
	if char not in word1a:
		word1a[char] = 1
	else:
		word1a[char] = word1a[char] + 1
for char in word1a:
	print(word1a[char])
	if word1a[char] > 3:
		print("These are not anagrams.")
	elif word1a[char] == 2:
		print("These are anagrams.")