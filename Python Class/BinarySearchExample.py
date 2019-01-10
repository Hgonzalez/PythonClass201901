def binary_search(alist, num):
	start = 0
	end = len(alist)-1
	
	exists = False
	
	while start<=end and not exists:
		midpoint = (start + end)//2
		if alist[midpoint] == num:
			exists = True
		else:
			if num < alist[midpoint]:
				end = midpoint-1
			else:
				start = midpoint+1
	
		return exists
	
testlist = [0,1,2,3,4,5,6,7]
print(binary_search(testlist, 100))