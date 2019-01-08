def count(some_list,to_count):
	x = 0
	for a in some_list:
		if a == to_count:
			x = x + 1
	return x
	
a = [1,2,3,5,4,2,4,6,3,5,5]

print(count(a,5))