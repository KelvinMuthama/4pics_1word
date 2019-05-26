"""This module holds the code for pattern matching the user's input  to give the probability of the word. Basically what happens is this, a uuser inputs the letters in the game and the length of the word, then the program gives the user all the possible words that can be formed by the letters given without repeating any letter. The words given are of the specified length given."""

import re
import sys

from words import words
english_words = words()

def user_input():
	letters = input("Enter the letters: ")

	try:
		length = eval(input("Enter the length of the word: "))
	except NameError:
		print("\nError!! \nEnter length in figures only eg : 4")
		sys.exit()

	pattern_to_match = '[' + letters + ']'  # This is the pattern the will be used by our re module

	lst_empty = []  # This list will hold all the matched words. However the list will contain duplicate letters.

	# This loop loops throughout the whole set for a word that matches the user's input.
	for word in english_words:
		word_match = re.findall(pattern_to_match, word)
		if len(word_match)== length and ''.join(word_match) in english_words:
			complete_word = ''.join(word_match)
			lst_empty.append(complete_word)

		# Convert lst_empty to a set to remove duplicate words in the list
		set_empty = set(lst_empty)


