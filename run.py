import random


class BaseBoard:
    """Base class for the game board,
    containing common properties and methods."""

    def __init__(self, grid_size, num_ships):
        """Initializes the grid size, number of ships,
        grid, and places the ships on the grid."""
        self.grid_size = grid_size
        self.num_ships = num_ships
        self.grid = self.create_grid()
        self.place_ships()

    def create_grid(self):
        """Creates and returns an empty grid of the specified size."""
        return [[' ' for _ in range(self.grid_size)]
                for _ in range(self.grid_size)]

    def place_ships(self):
        """Randomly places the specified number of ships on the grid."""
        for _ in range(self.num_ships):
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            while self.grid[row][col] == 'S':
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - 1)
            self.grid[row][col] = 'S'

    def print_board(self):
        """Prints the current state of the grid."""
        print("   " + " ".join([str(i) for i in range(len(self.grid))]))
        print("  " + "--" * len(self.grid))
        row_number = 0
        for row in self.grid:
            print("%d |%s|" % (row_number, "|".join(row)))
            row_number += 1
        print("\n")


class PlayerBoard(BaseBoard):
    """Class for the player's board, derived from the BaseBoard class."""

    def __init__(self, grid_size, num_ships, player_name):
        """Initializes the player's name and calls the parent constructor."""
        super().__init__(grid_size, num_ships)
        self.player_name = player_name

    def display(self):
        """Displays the player's board."""
        print("{}'s Board:".format(self.player_name))
        self.print_board()


class ComputerBoard(BaseBoard):
    """Class for the computer's board, derived from the BaseBoard class."""

    def display(self):
        """Displays the computer's board with ships hidden."""
        print("Computer's Board:")
        hidden_grid = [[' ' if cell == 'S' else cell for cell in row]
                       for row in self.grid]
        self.print_hidden_board(hidden_grid)

    def print_hidden_board(self, hidden_grid):
        """Prints the current state of the hidden grid."""
        print("   " + " ".join([str(i) for i in range(len(hidden_grid))]))
        print("  " + "--" * len(hidden_grid))
        row_number = 0
        for row in hidden_grid:
            print("%d |%s|" % (row_number, "|".join(row)))
            row_number += 1
        print("\n")


def get_computer_input(grid_size):
    """Generates random row and column coordinates within the grid size,
    for the computer's move."""
    row = random.randint(0, grid_size - 1)
    col = random.randint(0, grid_size - 1)
    return row, col


def get_user_input(grid_size):
    """Prompts the user for row and column coordinates within the grid size."""
    while True:
        try:
            row = int(input("Enter number horizontally between (0-{}): "
                            .format(grid_size - 1)))
            if 0 <= row < grid_size:
                break
            else:
                print("Invalid input, please enter coordinates within"
                      " the grid.\n")
        except ValueError:
            print("Invalid input, please enter a number.\n")

    while True:
        try:
            col = int(input("Enter number vertically between (0-{}): "
                            .format(grid_size - 1)))
            if 0 <= col < grid_size:
                break
            else:
                print("Invalid input, please enter coordinates within"
                      " the grid.\n")
        except ValueError:
            print("Invalid input, please enter a number.\n")
    return row, col


def main():
    """
The main function contains two primary loops:

The game loop:
This while loop continues running until either the user or the computer
has no remaining ships. Inside this loop, the player and computer boards
are displayed, and turns for the user and computer are handled.

a. User's turn loop:
This loop prompts the user to input their guess (row and column) for
a ship on the computer's board. It keeps asking for input until
the user provides a valid guess (a location that hasn't been guessed before).
Afterward, the loop checks if the guess is a hit or a miss,updates
the computer's board, and adjusts the scores and remaining ships accordingly.

b. Computer's turn loop:
This loop generates random guesses for the computer's turn.
It keeps generating new guesses until a valid guess
(a location that hasn't been guessed before) is found.
The loop then checks if the guess is a hit or a miss on the user's board
updates the user's board,
and adjusts the scores and remaining ships accordingly.

After the game loop ends, the main function prints the game results,
indicating whether the user or the computer has won the game."""

    print("--------------------------------")
    print("Welcome To The Battleships Game!")
    print("--------------------------------\n")
    print("Symbols explanation:\n")
    print(" S - Ship")
    print(" X - Hit")
    print(" 0 - User Miss on Computer's Grid")
    print(" # - Computer Hit")
    print("\n")

    player_name = input("Enter your name: ")

    while True:
        try:
            grid_size = int(input("Enter grid size (3 TO 15): "))
            if 3 <= grid_size <= 15:
                break
            else:
                print(f"Invalid input,please enter a grid size between"
                      f" 3 and 15 (inclusive).\n")
        except ValueError:
            print("Invalid input, please enter a number.\n")

    while True:
        try:
            num_ships = int(input("Enter number of ships (1 TO {}): \n"
                            .format(grid_size)))

            if 0 < num_ships <= grid_size:
                break
            else:
                print(f"Invalid input, please enter a number of ships"
                      f" between 1 and {grid_size} (inclusive).\n")

        except ValueError:
            print("Invalid input, please enter a number.\n")

    player_board = PlayerBoard(grid_size, num_ships, player_name)
    computer_board = ComputerBoard(grid_size, num_ships)

    user_score = 0
    computer_score = 0

    user_ships_remaining = num_ships
    computer_ships_remaining = num_ships

    while user_ships_remaining > 0 and computer_ships_remaining > 0:
        player_board.display()
        computer_board.display()

        # User's turn
        while True:
            row, col = get_user_input(grid_size)

            if (computer_board.grid[row][col] == ' ' or
               computer_board.grid[row][col] == 'S'):

                break
            else:
                print("You have already guessed this location try again.\n")

        # Check hit or miss on computer's board
        if computer_board.grid[row][col] == 'S':
            print(" YOU GOT Hit!\n")
            computer_board.grid[row][col] = 'X'
            computer_ships_remaining -= 1
            user_score += 1
        elif computer_board.grid[row][col] == ' ':
            print("\nYOU Miss!\n")
            computer_board.grid[row][col] = '0'

        # Computer's turn
        row, col = get_computer_input(grid_size)
        while (player_board.grid[row][col] == 'O' or
               player_board.grid[row][col] == 'X' or
               player_board.grid[row][col] == '#'):
            row, col = get_computer_input(grid_size)

        if player_board.grid[row][col] == 'S':
            print("Computer got a hit!\n")
            player_board.grid[row][col] = '#'
            user_ships_remaining -= 1
            computer_score += 1
        else:
            print("Computer missed!\n")

        print("User score: {}\nComputer score: {}\n"
              .format(user_score, computer_score))

    if user_ships_remaining == 0:
        print(f"The computer has sunk all of your ships!"
              f" Better luck next time!\n")
    else:
        print(f"Congratulations, {player_name}!"
              f" You have sunk all the computer's ships!\n")


if __name__ == "__main__":
    main()
