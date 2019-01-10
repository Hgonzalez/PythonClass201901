alist = [3,7,4,6,5]

def bubblesort(x):
	for _ in range(len(alist)-1):
		for i in range(0,len(alist)-1,1):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	print(alist) 

bubblesort(alist)