import copy
import random

def new_game():
	board = {2: [4, 4, 4, 4, 4, 4],
		 	1: [4, 4, 4, 4, 4, 4]}

	points = {1: 0, 2: 0}
	return(board, points)

def print_board(user, board, points, players):
	if players == '2':
		user2=[1,2]; user2.remove(user); user2=user2[0]
		board2 = copy.deepcopy(board[user2])
		board2.reverse()
		print("-------------------------------")
		print("| {}: {:2} {}    |".format(user2,points[user2],board2))
		print("| {}:    {} {:2} |".format(user,board[user],points[user]))
		print("-------------------------------")
	else:
		board2 = copy.deepcopy(board[2])
		board2.reverse()
		print("-------------------------------")
		print("| {}: {:2} {}    |".format(2,points[2],board2))
		print("| {}:    {} {:2} |".format(1,board[1],points[1]))
		print("-------------------------------")

def choose_cup(user, board, players):
	to_print=['quit','Quit']
	for i in range(6):
		cup = board[user][i]
		if cup>0:
			to_print.append(str(i+1))

	if players == '1' and user == 2:
		choice = random.choice(to_print[2:])
		print("Player 2: {}".format(choice))
		return(choice)

	choice=0
	while choice not in to_print:
		choice=input("Player {}: Choose from cups {} > ".format(user,', '.join(to_print[2:])))
		if choice in ('help','Help'):
			get_help()
	return(choice)

def play_choice(user,choice,board,points):
	user2=[1,2]; user2.remove(user); user2=user2[0]; skip=0
	moves = board[user][choice-1]
	board[user][choice-1] = 0

	for i in range(moves):
		add, cup = analyze_move(choice,i,board)

		if add == 'add_to_user1':
			board[user][cup] += 1
			print('{}. user{} cup {}'.format(i+1,user,cup+1))
			if i == moves-1 and board[user][cup] == 1:
				points[user] += (board[user][cup]+board[user2][5-cup])
				board[user][cup] = 0
				board[user2][5-cup] = 0
				print("user{} stole user{} cup {}".format(user,user2,(6-cup)))
		elif add == 'add_to_user2':
			board[user2][cup] += 1
			print('{}. user{} cup {}'.format(i+1,user2,cup+1))
		elif add == 'add_point':
			points[user] += 1
			print('{}. add point'.format(i+1))
			if i == moves-1:
				print("user{} gets another turn".format(user))
				skip=1

	return(board,points,skip)

def analyze_move(start,move,board):
	cup = start+move
	if cup < 6:
		return('add_to_user1',cup)
	elif cup>12 and cup<19:
		return('add_to_user1',cup-13)
	elif cup == 6 or cup == 20:
		return('add_point',6)
	elif cup >6 and cup<13:
		return('add_to_user2',cup-7)
	elif cup >20 and cup<27:
		return('add_to_user2',cup-21)

	else:
		print("There was an error.")
		print("cup={}, start={}, move={}".format(cup,start,move))

def calculate_score(board,points):
	points[1] = points[1] + sum(board[1])
	points[2] = points[2] + sum(board[2])
	return(points)

def get_help():
	print("INSTRUCTIONS")
	print("You will play against the computer or against a friend.")
	print("Take turns selecting a cup.")
	print("One point from the cup will be placed in each following")
	print(" cup, including your score, until the points are gone.")
	print("If the last point lands on your score, you go again.")
	print("If the last point lands in an empty space on your side,")
	print(" you may steal the opposing cup's points.")
	print("Play until one side of the baord is empty.")
	print("The player with the most points wins!")

def main():

	print("Want to play Mancala?")
	print("1: 1 player")
	print("2: 2 players")
	print("3: instructions")
	print("0: quit")

	players = input(" > ")
	board, points = new_game()
	user = 1
	
	if players in ('0','quit','Quit'):
		print("You quit.")
		return()
	elif players in ('3','help','Help','Instructions','instructions'):
		get_help()
		return()

	while any(board[1]) and any(board[2]):

		print_board(user,board,points,players)

		choice = choose_cup(user,board,players)
		if choice in ('quit','Quit'):
			print("You quit.")
			break
		else:
			choice = int(choice)

		board, points, skip = play_choice(user,choice,board,points)

		if not skip:
			if user == 1:
				user = 2
			elif user == 2:
				user = 1

	if choice not in ('quit','Quit'):
		print_board(user,board,points,players)
		print("The game has ended.")
		points = calculate_score(board,points)

		if points[1]>points[2]:
			print("Congratulations! Player 1 has won mancala!")
		elif points[2]>points[1] and players=='2':
			print("Congratulations! Player 2 has won mancala!")
		else:
			print("Oh no! You lost to the computer.")
		print("*Final*  Player1: {}  Player2: {}".format(points[1],points[2]))



main()


