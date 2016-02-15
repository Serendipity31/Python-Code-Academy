#Battleship Game

from random import randint

#the function play has the game actions
def play():
	board = []

	#This creates a 'board' consisting of 5 lists, each of which consists of 5 0's
	for x in range(0, 5):
		board.append(["O"] * 5)
		
	#This joins the 5 0's within each list into one row and prints them as rows
	def print_board(board):
		for row in board:
			print " ".join(row)
	
	#This shows the board
	print_board(board)

	#This defines the row coordinate for the ship location
	def random_row(board):
		return randint(0, len(board) - 1)

	#This defines the column coordinate for the ship location
	def random_col(board):
		return randint(0, len(board[0]) - 1)

	ship_row = random_row(board)
	ship_col = random_col(board)

    #ship location for debugging
	print "ship row: %d" % (ship_row)
	print "ship col: %d" % (ship_col)

	#This for loop gives users 4 turns to guess the location of the ship
	for turn in range(4):
		print "Turn", turn + 1 #note that turn didn't need to be initialized to 0 in this language
		guess_row = int(raw_input("Guess Row:"))
		guess_col = int(raw_input("Guess Col:"))
        
        # This compares the guess coordinates to the ship coordinates
		if guess_row == ship_row and guess_col == ship_col:
			print "Congratulations! You sank my battleship!"
			again()
			break
		else:
			if guess_row not in range(5) or guess_col not in range(5):
				print "Oops, that's not even in the ocean."
				if turn == 3:
				    outcome = "Game Over."
				    print outcome
				    again()
				    break
			elif board[guess_row][guess_col] == "X":
				print "You guessed that one already."
				if turn == 3:
				    outcome = "Game Over."
				    print outcome
				    again()
				    break
			else:    
				print "You missed my battleship!"
				board[guess_row][guess_col] = "X"
				if turn == 3:
				    print_board(board)
				    outcome = "Game Over."
				    print outcome
				    again()
				    break				    
			print_board(board)

#Calls the function play to run the game
play()

play_again = raw_input("Do you want to play again?")
if play_again == "Y":
    print "OK"