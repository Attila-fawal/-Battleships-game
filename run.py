import random
"""
This function creates an empty grid of the given size with all elements set to a space character (' ').
"""
def create_grid(grid_size):
    return [[' ' for _ in range(grid_size)] for _ in range(grid_size)]


"""
This function displays the user's grid to the user by calling the print_board(board) function.
"""
def display_user_grid(grid, player_name):
    print("{}'s Board:".format(player_name))
    print_board(grid)


"""
This function displays the computer's grid to the user without showing the ships by calling the print_board(board) function. Ships are replaced by spaces before printing.
"""
def display_computer_grid(grid):
    print("Computer's Board:")
    hidden_grid = [[' ' if cell == 'S' else cell for cell in row] for row in grid]
    print_board(hidden_grid)

"""
 This function generates a random row and column for the computer's move. It returns the row and column.
 """
def get_computer_input(grid_size):
    row = random.randint(0, grid_size - 1)
    col = random.randint(0, grid_size - 1)
    return row, col


"""
This function randomly places a specified number of ships ('S') on the given grid. It iterates through the number of ships and places them in random positions on the grid while making sure not to place a ship on top of another ship.
"""
def place_ships(grid, num_ships):
    for _ in range(num_ships):
        row = random.randint(0, len(grid) - 1)
        col = random.randint(0, len(grid) - 1)
        while grid[row][col] == 'S':
            row = random.randint(0, len(grid) - 1)
            col = random.randint(0, len(grid) - 1)
        grid[row][col] = 'S'

"""
 This function displays the grid to the user by calling the print_board(board) function.
"""
def display_grid(grid):
    print_board(grid)
"""
This function prints the board with coordinates. It displays row and column numbers on the top and left sides of the grid, and displays the grid's content row by row.
"""
def print_board(board):
    print("   " + " ".join([str(i) for i in range(len(board))]))
    print("  " + "--" * len(board))
    row_number = 0
    for row in board:
        print("%d |%s|" % (row_number, "|".join(row)))
        row_number += 1
    print("\n")
"""
 This function prompts the user for row and column input and validates it to make sure it's a valid coordinate within the grid. It returns the row and column entered by the user.
"""
def get_user_input(grid_size):
    while True:
        try:
            row = int(input("Enter number horizontally between (0-{}): ".format(grid_size - 1)))
            if 0 <= row < grid_size:
                break
            else:
                print("Invalid input, please enter coordinates within the grid.")
        except ValueError:
            print("Invalid input, please enter a number.")
    
    while True:
        try:
            col = int(input("Enter number vertically between (0-{}): ".format(grid_size - 1)))
            if 0 <= col < grid_size:
                return row, col
            else:
                print("Invalid input, please enter coordinates within the grid.")
        except ValueError:
            print("Invalid input, please enter a number.")


"""
The main function starts and runs the Battleships game. It initializes the game by:

1. Welcoming the player and explaining the symbols used in the game.
2. Asking for the player's name.
3. Prompting the player to choose the grid size between 3 and 15 (inclusive).
4. Prompting the player to choose the number of ships between 1 and the selected grid size (inclusive).
5. Creating the user's and computer's grids based on the chosen grid size.
6. Placing the ships on the user's and computer's grids.
7. Initializing the user and computer scores and ships remaining.

Then, the function enters the game loop where it alternates between the user's and computer's turns. During each turn:

1. Display the user's and computer's grids.
2. Get the user's guess for the computer's grid and check if it's a hit or a miss. Update the scores and remaining ships accordingly.
3. Get the computer's guess for the user's grid and check if it's a hit or a miss. Update the scores and remaining ships accordingly.

The game loop continues until either the user or the computer sinks all of the opponent's ships. At the end of the game, the function displays the appropriate win or lose message for the user.
"""


def main():
    print("Welcome To The Battleships Game!\n")
    print("Symbols explanation:")
    print(" S - Ship")
    print(" X - Hit")
    print(" O - User Miss")
    print(" 0 - User Miss on Computer's Grid")
    print(" # - Computer Hit")
    print(" C - Computer Miss")
    print("\n")

    player_name = input("Enter your name: ")

    while True:
        try:
            grid_size = int(input("Enter grid size (3 TO 15): "))
            if 3 <= grid_size <= 15:
                break
            else:
                print("Invalid input, please enter a grid size between 3 and 15 (inclusive).")
        except ValueError:
            print("Invalid input, please enter a number.")

    while True:
        try:
            num_ships = int(input("Enter number of ships (1 TO {}): ".format(grid_size)))
            if 0 < num_ships <= grid_size:
                break
            else:
                print("Invalid input, please enter a number of ships between 1 and {} (inclusive).".format(grid_size))
        except ValueError:
            print("Invalid input, please enter a number.")

    user_grid = create_grid(grid_size)
    computer_grid = create_grid(grid_size)

    place_ships(user_grid, num_ships)
    place_ships(computer_grid, num_ships)

    user_score = 0
    computer_score = 0

    user_ships_remaining = num_ships
    computer_ships_remaining = num_ships

    while user_ships_remaining > 0 and computer_ships_remaining > 0:
        display_user_grid(user_grid, player_name)
        display_computer_grid(computer_grid)

        # User's turn
        row, col = get_user_input(grid_size)

        if computer_grid[row][col] == 'S':
            print(" YOU GOT Hit!")
            computer_grid[row][col] = 'X'
            user_grid[row][col] = 'X'
            computer_ships_remaining -= 1
            user_score += 1
        elif user_grid[row][col] == ' ':
            print("YOU Miss!")
            user_grid[row][col] = 'O'
            computer_grid[row][col] = '0'
        else:
            print("You have already guessed this location.")

        # Computer's turn
        row, col = get_computer_input(grid_size)
        while user_grid[row][col] == 'O' or user_grid[row][col] == 'X' or user_grid[row][col] == '#' or user_grid[row][col] == 'C':
            row, col = get_computer_input(grid_size)

        if user_grid[row][col] == 'S':
            print("Computer got a hit!")
            user_grid[row][col] = '#'
            user_ships_remaining -= 1
            computer_score += 1
        else:
            print("Computer missed!")
            user_grid[row][col] = 'C'

        print("User score: {}\nComputer score: {}".format(user_score, computer_score))

    if user_ships_remaining == 0:
        print("The computer has sunk all of your ships! Better luck next time!")
    else:
        print("Congratulations, {}! You have sunk all the computer's ships!".format(player_name))

if __name__ == "__main__":
    main()
