def word_usage(pipe):
	punc = [".", ",", "?", "!", "%", "#", "@", "&", "*", '"']
		
	for char in pipe:
		if char in punc:
			pipe = pipe.strip(char)
	return pipe
def tuple_unpack(t):
	return t[1]

with open("/Users/hiramgonzalez/Downloads/article.txt", "r", encoding="utf-8") as data:
	
	words = data.read().lower().split()
	count = {}
	
	for alpha in words:
		fict = word_usage(alpha)
		if fict not in count:
			count[fict] = 1
		else:
			count[fict] = count[fict] + 1
	alist = list(count.items())	
	alist.sort(key=tuple_unpack, reverse=True)	
	print(alist[0:10])		