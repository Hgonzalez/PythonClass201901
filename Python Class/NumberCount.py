alist = [1,3,55,1,9,4,56,2,1,8]

tally = 0
for number_one in alist:
	if number_one == 1:
		#print("counted 1.")
		#tally = tally + 1
		tally += 1
print(tally)