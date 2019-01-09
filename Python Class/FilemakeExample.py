s1 = "Hi How are you?\n"
s2 = str(55)

with open("/Users/hiramgonzalez/Desktop/myword.txt", "w", encoding="utf-8") as banana:
	banana.write(s1)
	banana.write(s2)