word = "apple"

letter = "l"

for banana in range(len(word)):
	if letter == word[banana]:
		print(word[banana])
		Slice = banana
		word1 = word[0:Slice]
		word2 = word[Slice+1:]
		finalword = word1 + "w" + word2
		print(finalword)
		
		
