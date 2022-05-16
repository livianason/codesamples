import wordlists
import random

def choose_category():
	print("Enter a category number:")
	print("1. Animals")
	print("2. Fruit")
	print("3. Vegetables")
	print("4. Clothes")
	print("5. Beach")
	print("6. Ocean")
	print("7. Plants")
	print("8. Anatomy")
	print("9. Astronomy")
	options=['1','2','3','4','5','6','7','8','9']

	cat = input("Category #: ")
	while cat not in options:
		cat = input("That's not an option. Enter a category number: ")

	match cat:
		case '1':
			return(wordlists.animals)
		case '2':
			return(wordlists.fruit)
		case '3':
			return(wordlists.vegetables)
		case '4':
			return(wordlists.clothes)
		case '5':
			return(wordlists.beach)
		case '6':
			return(wordlists.ocean)
		case '7':
			return(wordlists.plants)
		case '8':
			return(wordlists.anatomy)
		case '9':
			return(wordlists.astronomy)

def print_hangman(tries):
	man = [ '-+--------+--+-',
			' |        |  |',
			' |        /  |',
			' |   (><)/   |',
			' |    {}/    |',
			' |   /||\\    |',
			' |    /\\     |',
			' |   /  \\    |',
			' |           |',
			'-+-----------+-']
	for i in range(tries):
		print(man[i])

def print_blanks(word, letter_bank):
	blanks=''
	guesses=[]

	if word in letter_bank:
		for w in word:
			letter_bank.append(w)
	
	for letter in word:
		if letter in letter_bank:
			blanks += letter
			guesses.append(letter)
		elif not letter.isalpha():
			blanks += letter
		else:
			blanks += '_'
			guesses.append(0)

	print('|'+(len(word)+2)*'-'+'|')
	print('| '+blanks+' |')
	print('|'+(len(word)+2)*'-'+'|')
	return(guesses)

def get_guess(used, guess='-'):
	while (guess in used) or (not guess.isalpha()):
		guess = input("Guess a letter: ")

	if guess in ('quit','Quit') or len(guess) == 1:
		return(guess)
	else: 
		return(submit_word(used,guess.lower()))
		

def submit_word(used, guess):
	print("Submit this word? '{}'".format(guess))
	flag = input("Y/N? > ")
	if flag in ('n','N'):
		return(get_guess(used))
	elif flag in ('y','Y'):
		return(guess)



# 1. Pick a category
category = choose_category()
word = random.choice(category).lower()


used_letters = []
guesses = print_blanks(word, used_letters)
fails = 0

while fails < 10 and not all(guesses):
	
	if len(used_letters) > 0:
		print("Used: {}".format(used_letters))

	letter_guess = get_guess(used_letters)
	
	if letter_guess=='quit':
		break

	used_letters.append(letter_guess.lower())

	old_count = guesses.count(0)
	guesses = print_blanks(word,used_letters)
	new_count = guesses.count(0)

	if new_count == old_count:
		fails += 1
	elif all(guesses):
		break
	
	print("{} fails left.".format(10-fails))

	print_hangman(fails)

if all(guesses):
	print("Congratulations! You beat Hangman!")
else:
	print("You lost.")
	print("The word was: {}".format(word))
	





