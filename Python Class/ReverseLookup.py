fte = {'le':'the', 'la':'the','chat':'cat','livre':'book','pomme':'apple'}
search_param = input("Enter a word to translate:\n> ")

def reverse_lookup(dictionary,word):
	capture = []
	for e in dictionary.keys():
		if search_param == dictionary[e]:
			capture.append(e)
	return capture
print(reverse_lookup(fte, search_param))
