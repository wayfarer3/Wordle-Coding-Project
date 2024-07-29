# intro message
print("This is an unlimited version of Wordle, a word guessing game. Guess the Wordle in six tries, each guess has to be a valid five letter word.")

# importing the colour
from termcolor import colored as coloured
from random_word import get_random_word

# importing PySpellChecker to check words
from spellchecker import SpellChecker
spell = SpellChecker()

# importing replit module for replit.clear()
import replit

# setting up the timer
import time
start_time = time.time()

# counting variables
plays, guesses = 1, 0

# asking the user for their input and checking it
def ask():
	global guesses
	word = input("\nYour guess: ")
	if word.isalpha() and len(word) == 5 and word == spell.correction(word):
		guesses += 1
		return(word.upper())
	elif not word.isalpha():
		print("Please enter a word, no numbers or symbols.")
		ask()
	elif not len(word) == 5:
		print("Please enter five-letter word.")
		ask()
	else:
		print("Please enter an English word.")
		ask()


# checks if the letters match and colours the word (green = correct, yellow = in word, red = not in word)
def colour(guess, answer):
	global random_word_list
	coloured_str, coloured_yellow, coloured_green = "", [], []
	for i in range(len(guess)):
		if guess[i] == answer[i]:
			coloured_str += coloured(guess[i],"green")
			coloured_green.append(guess[i])
		elif guess[i] in random_word_list:
			if sum(s.count(guess[i]) for s in random_word_list) == sum(s.count(guess[i]) for s in guess):
				coloured_str += coloured(guess[i],"yellow")
			elif sum(s.count(guess[i]) for s in guess) < sum(s.count(guess[i]) for s in random_word_list) and not guess[i] in coloured_yellow and not guess[i] in coloured_green:
				coloured_str += coloured(guess[i],"red")
			elif sum(s.count(guess[i]) for s in guess) > sum(s.count(guess[i]) for s in random_word_list) and not guess[i] in coloured_yellow and not guess[i] in coloured_green:
				coloured_str += coloured(guess[i],"red")
			elif sum(s.count(guess[i]) for s in random_word_list) > sum(s.count(guess[i]) for s in coloured_yellow) + sum(s.count(guess[i]) for s in coloured_green):
				coloured_str += coloured(guess[i],"yellow")
				coloured_yellow.append(guess[i])
			else:
				coloured_str += coloured(guess[i],"red")
		else:
			coloured_str += coloured(guess[i],"red")
	return(coloured_str)

# asks if player wants to replay, if not then outputs game statistics
def replay():
	global plays, guesses
	replay = input("\nDo you want to play again? (yes to continue)\n")
	if str(replay) == "yes":
		plays += 1
		replay = ""
		return(True)
	else:
		elapsed_time = round(time.time() - start_time, 2)
		print("\n\nGAME STATISTICS\n\nTotal guesses: " + str(guesses) + "\nTotal plays: " + str(plays) + "\nTotal time taken: " + str(elapsed_time) + "\nAverage guess per word: " + str(round(guesses/plays,2)) + "\nAverage time per word: " + str(round(elapsed_time/plays,2)) + "\nAverage time per guess: " + str(round(elapsed_time/guesses,2)))
		exit()
	
# runs the game - generates random word and loops the functions until all is correct, stops when player decides to end session
def run():
	global plays, guesses
	random_word = get_random_word().upper()
	global random_word_list
	random_word_list = list(random_word)
	guesses_list = ["This is an unlimited version of Wordle, a word guessing game. Guess the Wordle in six tries, each guess has to be a valid five letter word."]
	#print(random_word) # comment out later 
	while True:
		guess = ask()
		try:
			coloured_guess = colour(guess,random_word)
			print(coloured_guess)
		except TypeError:
			print("Error, please try again.")
			guesses -= 1
		else:
			replit.clear()
			guesses_list.append(coloured_guess)
			for item in guesses_list:
				print(item)
		if random_word == guess:
			print("\nSolved.")
			if replay():
				run()
		elif len(guesses_list) > 6:
			print("\nYou've used up your six chances. The word was \"" + random_word + "\", too bad.")
			if replay():
				run()

run()
# problems in the code:
#		Sometimes there are unexpected NoneType errors (half solved with try/except)
#		when asking for a replay the program should stop the timer