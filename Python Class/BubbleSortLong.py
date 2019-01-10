def bubblesort(x):
	holder = 0
	#blist = x
	for numbers in range(len(x)-1):
		#print(numbers)
		dontcare = numbers+1
		#print(dontcare)
		if x[numbers] > x[dontcare]:
			holder = x[numbers]
			x[numbers] = x[dontcare]
			x[dontcare] = holder

alist = [3,7,4,6,5,2,1]
blist = []

for _ in range(len(alist)-1):
	bubblesort(alist)
#print("Original list: {}".format(blist))
print(alist)
