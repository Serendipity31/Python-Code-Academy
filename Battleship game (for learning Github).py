#Battleship Game
#Extra Credit take 1

from random import randint

#function allows users to loop through the programme as many times as they want
def again():
    play_again = raw_input("Do you want to play again?").lower()
    if play_again == "n":
        print "OK. Goodbye"
    elif play_again == "y":
        print "OK. Let's play again."
        play()
    else:
        print "Error. Please put Y for yes and N for no."
        play_agagin = ""
        play_again = raw_input("Do you want to play again?").lower()
        if play_again == "n":
            print "OK. Goodbye"
        elif play_again == "y":
            print "OK. Let's play again."
            play()


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

'''A note on the again() function. 

I tried getting this option of playing again to work in several ways. 

All of them involved moving all of the 'action' part of the game into a function, 
so that I could then call that function repeatedly.

The first way was just using an if/else statement that was called after play()
finished. That worked to loop it through once if the user typed 'y' in response to the question posed. 
It would call play() for the second time, and then that was it. The reason is that python isn't actually 
reading to the top of the page again. It executed the contents of play(), and that didn't have anything to 
do with the question to play again or not, so it stopped. 

The second way I tried was with a while loop that had if/else statements within it. It looked like this:

while True:
	play_again = raw_input("Do you want to play again?").lower()
    if play_again == "n":
        print "OK. Goodbye"
    elif play_again == "y":
        print "OK. Let's play again."
        play()

The problem here was that this while loop was only being called the once, and so play_again was 
only being requested once and only set once. That means that it was set within that while loop, and subsequent 
attempts to combine this with over-writing the value of play_again elsewhere in the programme
didn't work. If I hit 'y' first, then the game would go on indefinitely with no break. If it hit 'n' the game
ended. 

The third way I tried was to ask for the raw_input within play(), but then to try and call on the
variable play_again outside of the play() function. That turned play_again into a local variable, 
so that didn't work.

Finally, I realized that each time play() was executed, it needed to call a function that asked
whether the user wanted to play again. And then, that function in turn had to call play() when 
the user answered with a 'Y'. Furthermore, this again() function had to be called for each option
in the else statement above at the point that all 4 turns were over, so that no matter what choices 
were made, the user could play again.

Key lesson: even though I think of looping through the script as starting at the top of the page and
working my way down, Python does not. The functions are discrete pieces of code that are only shown
vertically on the page because that is the only way we can type them....If there is nothing in a function
pointing to another set of commands, those commands won't get executed repeatedly just because they are beneath		
other commands on the page.

Note that it has to be above the play() function so it is defined when is called.
'''