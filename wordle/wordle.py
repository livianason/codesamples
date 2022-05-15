import words
import random


def get_result(guess, answer):
	answer_dict = check_for_dup_letters(answer)

	result=['_','_','_','_','_']
	for i in range(5):
		if guess[i] == answer[i]:
			result[i] = "O"
			answer_dict[guess[i]] -= 1
			
	for i in range(5):
		if guess[i] == answer[i]:
			None
		elif (guess[i] in answer) and (answer_dict[guess[i]] >0):
			result[i] = "X"
			answer_dict[guess[i]] -= 1

	concat = ''
	for r in result:
		concat += r

	return(concat)

def check_for_dup_letters(answer):
	answer_dict = {}
	for letter in answer:
		if letter in answer_dict:
			answer_dict[letter] += 1
		else:
			answer_dict[letter] = 1
	return(answer_dict)

def get_help():
	print("* HELP MENU:")
	print(" *  I - instructions")
	print(" *  R - results")
	print(" *  Q - quit")
	print(" *  X - continue")
	flag=input(" > ")

	if flag in ('Q','q','quit','Quit'):
		return('q')
	elif flag in ('R','r','result','results','Results','Result'):
		return('r')
	elif flag in ('I','i','instructions','Instructions'):
		print("* INSTRUCTIONS:")
		print(" * A 5 letter word is selected at random.")
		print(" * You must guess the word within 6 tries.")
		print(" * After each guess, the accuracy result will print.")
		print(" * Result Meaning:")
		print(" * O : a correct letter is in the correct position")
		print(" * X : a correct letter is in the wrong position")
		print(" * _ : the letter does not appear in the final word.")
		print(" * Input q to quit, r for results, or x to continue.")
		flag=input(" > ")
	return(flag)

def print_results(guesses,results):
	if len(guesses) <1:
		print("* You have not made any quesses.")
	else:
		print("* YOUR RESULTS:")
		for i in range(len(guesses)):
			print('{}: {}'.format(i+1, guesses[i]))
			print('{}: {}'.format(i+1, results[i]))


##### BEGIN GAME CODE HERE #####

answer = random.choice(words.ans_words).lower()
#print(answer)

print("* Guess a 5 letter word.")
print("* You can also enter 'quit' or 'help'")


all_guesses=[]
all_results=[]

for tries in range(6):
	guess=input(str(tries+1)+"> ").lower()
	flag='x'

	while (guess not in words.word_list) or (guess in (all_guesses)):
		if guess in ('quit','Quit'):
			flag='q'
			break
		elif guess in ('help','Help'):
			flag=get_help()
			if flag == 'q':
				break
			elif flag == 'r':
				print_results(all_guesses,all_results)
			else:
				None
		elif guess in ('results','Results'):
			print_results(all_guesses,all_results)
		elif guess in all_guesses:
			print("* You already guessed this word.")
		else:
			print("* Enter a real 5 letter word.")
			print("* Or 'results', 'quit' or 'help'")

		guess=input(str(tries+1)+"> ")


	if flag == 'q':
		print("* You quit.")
		print("* The word was: "+answer)
		break
	else:
		result = get_result(guess,answer)
		all_guesses.append(guess)
		all_results.append(result)
		print ("   "+result)
		

	if guess == answer:
		print("* Congratulations! You beat Wordle!")
		break
	elif tries == 5:
		print("* You lost.")
		print("* The word was: "+answer)


	


