def NumberFinder(x,y):
	flag = True
	start = 0
	end = len(x)-1
	middle = int((start + end)//2)
	count = 0
	while flag == True:
		length = len(x)-1
		for i in range(len(x)):
			if y > x[length]:
				print("Your number, {}, is too long!".format(y))
				flag = False
				break
			elif x[i] == y:
				print("Your magic number was {}.".format(y))
				print("It took me {} tries to guess your number.".format(count))
				flag = False	
			else:
				if y > middle:
					end = middle + 1
					count += 1
				elif y > x[length]:
					flag = False
				else:
					start = middle - 1
					count += 1

user_lists = input("Enter a list of numbers:\n> ")
user_lists.split()
user_list = []
for i in user_lists:
	if i != " ":
		i = int(i)
		user_list.append(i)

	
user_number = int(input("Enter a magic number: \n> "))
user_list.sort()
NumberFinder(user_list, user_number)