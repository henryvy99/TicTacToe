# Written By Henry Vy
# This program is a tic tac toe game!
# It prints out the board using the print_board function, which takes in the given array (board) and assigns
# all of the elements to spaces(" ").

import random


# Definitions / Methods
def print_board(array):  # Prints the board
    print("\t0\t1\t2")
    for i in range(3):
        print(str(i), end='\t')
        for j in range(3):
            print(array[i][j] + "|\t", end='')
        print("\n\t__________")


def winner(array, string):  # Used to check who the winner is ([board], ["X" or "O"])
    if (array[0][0] == string and array[0][1] == string and array[0][2] == string
            or array[1][0] == string and array[1][1] == string and array[1][2] == string
            or array[2][0] == string and array[2][1] == string and array[2][2] == string

            or array[0][0] == string and array[1][0] == string and array[2][0] == string
            or array[0][1] == string and array[1][1] == string and array[2][1] == string
            or array[0][2] == string and array[1][2] == string and array[2][2] == string

            or array[0][0] == string and array[1][1] == string and array[2][2] == string
            or array[0][2] == string and array[1][1] == string and array[2][0] == string):
        print_board(array)  # Prints out the board for the winner!
        return True

    return False


# Main
again = True  # Used to prompt user if they want to play again
user_wins = 0  # Keeps track of the user's wins
comp_wins = 0  # Keeps track of the computer's wins

while again:
    board = [[" " for i in range(3)] for j in range(3)]  # Sets a 2d array with " "
    print_board(board)  # Prints the tic tac toe board

    num_spots = 0  # Used to stop the program if there are no more spaces on the tic tac toe board
    user_won = False

    while True:
        userX = int(input("Enter your X coordinate(row) or Enter negative number to quit: "))
        if userX < 0:
            break
        userY = int(input("Enter your Y coordinate(column) or Enter negative number to quit: "))
        if userY < 0:
            break

        while userX > 2:
            userX = int(input("Number too high! Try again: "))
        while userY > 2:
            userY = int(input("Number too high! Try again: "))
        while board[userX][userY] != " ":  # This while loop denys user to overwrite the spots
            userX = int(input("Spot taken! Enter your X coordinate(row): "))
            if userX < 0:
                break
            userY = int(input("Spot taken! Enter your Y coordinate(column): "))
            if userY < 0:
                break
        board[userX][userY] = "X"  # puts user's mark on the board
        num_spots += 1

        if winner(board, "X"):  # You win!
            print("You win")
            user_wins += 1
            user_won = True
            break

        if num_spots == 9:  # No more spots / TIE!
            print_board(board)
            print("No more spots! Tie Game!")
            break

        print("Computer's Turn")
        compX = random.randint(0, 2)
        compY = random.randint(0, 2)
        while board[compX][compY] != " ":
            compX = random.randint(0, 2)
            compY = random.randint(0, 2)
        board[compX][compY] = "O"
        num_spots += 1

        if winner(board, "O"):  # Computer wins!
            print("Computer win")
            comp_wins += 1
            break

        print_board(board)

    if user_won:  # If the user wins, then they have no choice but the play again
        print("Computer demands a rematch!")
    else:  # If the computer wins, the user can quit or play again
        play = input("Play again? (y/n): ")
        if play is "n":  # Ends the program
            print("User's Wins: " + str(user_wins))
            print("Computer's Wins: " + str(comp_wins))
            print("Bye! Thanks for playing")
            again = False
