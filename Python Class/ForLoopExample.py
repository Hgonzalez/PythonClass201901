alist = ["media","video","audio","cat"]

for i in range(0,len(alist),1):
	print(i,alist[i])
	
alist = ["media","video","audio","cat"]

for i in range(0,len(alist),1):
	alist[i] = alist[i].upper()
print(alist)

alist = ["media","video","audio","cat"]
for var1,var2 in enumerate(alist):
	print(var1,var2)