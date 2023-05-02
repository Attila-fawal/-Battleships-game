import random
"""
This function creates an empty grid of the given size with all elements set to a space character (' ').
"""
def create_grid(grid_size):
    return [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

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
This function is the main game loop. It initializes the game by setting the grid size, welcoming the player, and asking for the number of ships. It then creates the user's and computer's grids, places the ships on the computer's grid, and starts the game loop. In the loop, the user tries to guess the ship locations. If the user guesses correctly, the ship is marked as hit ('X') and the number of remaining ships is decreased. If the user guesses incorrectly, the location is marked as a miss ('O'). The game continues until all ships are sunk.
"""

def main():
    grid_size = 10

    print("Welcome To The Battleships Game!\n")

    while True:
        try:
            num_ships = int(input("Enter number of ships (1 TO 10): "))
            if 0 < num_ships <= grid_size:
                break
            else:
                print("Invalid input, please enter a number of ships between 1 and 10 (inclusive).")
        except ValueError:
            print("Invalid input, please enter a number.")

    user_grid = create_grid(grid_size)
    computer_grid = create_grid(grid_size)

    place_ships(computer_grid, num_ships)

    ships_remaining = num_ships

    while ships_remaining > 0:
        display_grid(user_grid)

        row, col = get_user_input(grid_size)

        if computer_grid[row][col] == 'S':
            print(" YOU GOT Hit!")
            computer_grid[row][col] = ' '
            user_grid[row][col] = 'X'
            ships_remaining -= 1
        elif user_grid[row][col] == ' ':
            print("YOU Miss!")
            user_grid[row][col] = 'O'
        else:
            print("You have already guessed this location.")

    print("Congratulations! You have sunk all the ships!")

if __name__ == "__main__":
    main()
