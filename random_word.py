import random

common_word_list = []

with open("common_five_letter_words.txt") as f:
	words = f.readlines()
	for word in words:
		word = word.strip()
		if len(word) == 5:
			common_word_list.append(word)

def get_random_word():
	return random.choice(common_word_list)