from random import randint


machine_numbers = []
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#This will print the board
def pri_board():
	print "\n\t%s | %s | %s\n\t- + - + -\n\t%s | %s | %s\n\t- + - + -\n\t%s | %s | %s\n" % (
	board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])

#Function that replaces a number with a simbol. If number doesn't exists, returns False
def replace(number, simbol):
	if number in board:
		del board[int(number) - 1]
		board.insert(int(number) - 1, simbol)
		return True
	else:
		return False

#Will check who's the winner
def check_win(who):
	message = "%s wins!" % who
	#Checks horizontals
	for x in (0, 3, 6):
		if board[0 + x] == board[1 + x] == board[2 + x]:
			print message
			exit(0)
	#Checks verticals
	for x in range(0, 3):
		if board[0 + x] == board[3 + x] == board[6 + x]:
			print message 
			exit(0)
	#Checks diagonals
	if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
		print message
		exit(0)
	#Check for tie
	if board.count("X") == 5 or board.count("O") == 5:
		print "No one wins :("
		exit(0)

#Player turn
def p_turn():
	print "Choose a free number."
	pri_board()
	if replace(raw_input("> "), "X") == True:
		pri_board()
		check_win('Player')
		m_turn()
	else:
		print "Invalid number.\n"
		p_turn()

#Machine turn
def m_turn():
	#Tries to replace a random number between 1 and 9
	if replace(str(randint(1, 9)), "O") == True:
		print "     - - - - - - - -"
		pri_board()
		check_win('Machine')
		p_turn()
	else:
		m_turn()

p_turn()
