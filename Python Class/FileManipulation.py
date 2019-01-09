banana = open("banana.txt", encoding="utf8")

banana.readline() #reads all the lines in the file, line by line.
banana.readlines() #reads only the first line.
banana.read() #reads the whole file, not indentation for new line.
banana.close() #closes the file.

with open("banana.txt", encoding="utf8") as banana:																			# this will open the file and pass each item in it to the variable banana, so you can use that item.
	print(banana.read())

with open("/Users/hiramgonzalez/Downloads/banana.txt", "w", encoding="utf8") as banana:																			# this will create the file and pass each item in it to the variable banana, so you can use that item.
	print(banana)