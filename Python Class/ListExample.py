alist = [1,2,3,5,3,2]
alist2 = [9,9]

alist.extend(alist2)

print(alist)

alist = [4,2,6]

alist[0] = 32289372

print(alist)

alist = [[3,2,4],[2,4,3],[4,2,9,6]]

print(alist[2])

print(alist[0][1])

alist = [["cat","dog","pig"],["boy","girl"],["media","video","audio","cat"]]

print(alist[0][1])

alist = [1,2,3,5,3,2]
blist = []
for	number in alist:
	if number == 2:
		blist.append(number)

print(blist)
print(len(blist))

alist = [1,2,3,5,3,2]
blist = [number for number in alist if number == 2]

print(blist)

alist = [1,2,3,5,3,2]
blist = [number*2 for number in alist]
print(blist)