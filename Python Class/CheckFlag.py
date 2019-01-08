palindrome = input("Enter a word: \n> ")

flagvariable = True

for c in range(len(palindrome)//2):
	print(c)
	print(len(palindrome)//2-1-c)
	if palindrome[c] != palindrome[len(palindrome)-1-c]:
		flagvariable = False
	
if flagvariable:
	print("This word {} is a palindrome".format(palindrome))
else:
	print("This word {} is NOT a palindrome".format(palindrome))
	
	#index each letter
	#compare each index using ord