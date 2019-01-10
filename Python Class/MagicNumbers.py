numb = int(input("Enter the magic number \n> "))
testlist =[0]

while numb not in testlist:
	numb2 = int(input("Enter the magic number \n> "))
	testlist.append(numb2)
	if numb < numb2:
		print("Down")
	elif numb > numb2:
		print("Up")
	else:
		print("Same")