alist = [2, 4, 7, 12, 15, 3]

for a in range(0,len(alist),1):
	if alist[a] >= 10:
		alist[a] = alist[a] * 2
	else:
		alist[a] = 0
print(alist)
