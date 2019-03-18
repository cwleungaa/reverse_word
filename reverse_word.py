words = input('Please enter a word: ')

word_list = []
word_dict = {}

for word in words:
	word_list.append(word)

for i in range(len(word_list)):
	word_dict[len(word_list) - i] = word_list[i]

for k in range(len(word_list)):
 	print(word_dict.get(k+1))





