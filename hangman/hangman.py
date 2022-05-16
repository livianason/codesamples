import wordlists
import random

def choose_category():
	categories=["1. Animals","2. Fruit","3. Vegetables","4. Clothes","5. Beach","6. Ocean","7. Plants","8. Anatomy","9. Astronomy"]
	print("Enter a category number:")
	for c in categories:
		print(c)

	options=['1','2','3','4','5','6','7','8','9']
	cat = input("Category #: ")
	while cat not in options:
		cat = input("That's not an option. Enter a category number: ")

	match cat:
		case '1':
			return(categories[int(cat)-1],wordlists.animals)
		case '2':
			return(categories[int(cat)-1],wordlists.fruit)
		case '3':
			return(categories[int(cat)-1],wordlists.vegetables)
		case '4':
			return(categories[int(cat)-1],wordlists.clothes)
		case '5':
			return(categories[int(cat)-1],wordlists.beach)
		case '6':
			return(categories[int(cat)-1],wordlists.ocean)
		case '7':
			return(categories[int(cat)-1],wordlists.plants)
		case '8':
			return(categories[int(cat)-1],wordlists.anatomy)
		case '9':
			return(categories[int(cat)-1],wordlists.astronomy)

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
	print('')

def print_blanks(word, letter_bank):
	blanks=''
	guesses=[] #list to determine if game is won or continue

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

	print('')
	print('|'+(len(word)+2)*'-'+'|')
	print('| '+blanks+' |')
	print('|'+(len(word)+2)*'-'+'|')
	return(guesses)

def get_guess(used, category):
	print('')
	det = 1
	while det:
		guess = input("Guess a letter: ")
		det = determine_guess(used,guess,category)

	return(guess)
		
# a, category, quit, help, answer
def determine_guess(used,guess,category):
	if guess in ['category','Category']:
		print("The category is: {}".format(category[3:]))
		return(1)
	elif guess in ['quit','Quit']: 
		q = input("Are you sure you want to quit? Y/N > ")
		if q in ['Y','y']:
			return(0)
		else:
			return(1)
	elif guess in ['Help','help']:
		get_help()
		return(1)
	elif len(guess) == 1 and guess.isalpha() and guess not in used:
		return(0)
	elif len(guess) > 1:
		return(submit_word(used,guess))
	else: 
		return(1)


def submit_word(used, guess):
	print("Submit this word? '{}'".format(guess))
	flag = input("Y/N > ")
	if flag in ('n','N'):
		return(1)
	elif flag in ('y','Y'):
		return(0)

def get_help():
	print('')
	print("INSTRUCTIONS:")
	print("First, you will select a word category.")
	print("A word from that category is chosen at random.")
	print("You must guess the word one letter at a time.")
	print("If you think you know the word, enter")
	print(" the whole word and confirm submission.")
	print("You have 10 failed guesses before the man is hanged.")
	print("Other options are 'help', 'quit', or 'category'")
	print('')

# 1. Pick a category
category,words = choose_category()
word = random.choice(words).lower()

print('')
print("The category is: {}".format(category[3:]))

used_letters = []
guesses = print_blanks(word, used_letters)
fails = 0

while fails < 10 and not all(guesses):
	
	if len(used_letters) > 0:
		print("Used: {}".format(used_letters))

	letter_guess = get_guess(used_letters,category)

	if letter_guess == 'quit':
		break

	used_letters.append(letter_guess.lower())

	old_count = guesses.count(0)
	guesses = print_blanks(word,used_letters)
	new_count = guesses.count(0)

	if new_count == old_count:
		fails += 1
	elif all(guesses):
		break
	
	print_hangman(fails)
	print("{} fails left.".format(10-fails))

	

if all(guesses):
	print("Congratulations! You beat Hangman!")
else:
	print("You lost.")
	print("The word was: {}".format(word))
	





