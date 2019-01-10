food = {}
food["fruit"] = ["watermelon", "apple"]
food["vegetable"] = ["broccoli", "kale"]
print(food)
print(food["fruit"])
print(food["fruit"][0])

directory = {}
directory["Hiram"] = {}
directory["Hiram"]["Number"] = 347321456
directory["Hiram"]["E-mail"] = "hiram.g@mail.com"
directory["Hiram"]["Hobby"] = "Python"
directory["bossman"] = {}
directory["bossman"]["Number"] = 3723452124
directory["bossman"]["E-mail"] = "bossman@mail.com"
directory["bossman"]["Hobby"] = "Data"

print(directory["Hiram"]["E-mail"])
print(directory["bossman"]["Number"])

data_people = []

for i in directory.keys():
	person = i
	fun = directory[i]["Hobby"]
	if fun == "Data":
		data_people.append(person)
print(data_people)