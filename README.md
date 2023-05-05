
# The Battleships game

A classic Battleships game where the player competes against the computer to sink each other's ships. The game features a variable grid size, the number of ships, and player input for making guesses. The objective is to sink all of the opponent's ships before they sink yours. Here is the live version of the project: https://battleships--game.herokuapp.com/

![Screenshot (48)](https://user-images.githubusercontent.com/127791713/236436098-a9a1fc2e-daf7-4dea-a819-d196fc5fec7b.png)

## Game Flow
- The game begins by asking the user for their name, grid size, and the number of ships.
- The player and computer boards are initialized with random ship placement.
- The game loop starts, with turns alternating between the player and computer.
- On the player's turn, they input their guess (row and column) for a ship on the computer's board.
- The computer's turn consists of randomly generated guesses.
- The game continues until either the user or the computer has no remaining ships.
- The result is displayed, showing whether the user or computer has won the game.

![Screenshot (49)](https://user-images.githubusercontent.com/127791713/236438040-eb700b77-9387-47c1-86b6-b98286a78284.png)
![Screenshot (42)](https://user-images.githubusercontent.com/127791713/236437505-55027573-85e5-4eb1-80be-9c68a9b5e60e.png)

## Error Handling
- The Battleships game has built-in error handling to manage incorrect user inputs, ensuring a smooth gameplay experience. If the user provides invalid input when prompted, the game will display an appropriate error message and ask the user to try again.

### Examples of Error Handling
- Grid size input: If the user enters a non-numeric input or a number outside the valid range (3-15), the game will display an error message and prompt the user to enter a valid grid size.

![Screenshot (52)](https://user-images.githubusercontent.com/127791713/236441430-689ea81d-6f04-462b-b3d4-5ec2a190496d.png)

- Number of ships input: If the user enters a non-numeric input or a number outside the valid range (1 to the grid size), the game will display an error message and prompt the user to enter a valid number of ships.

![Screenshot (50)](https://user-images.githubusercontent.com/127791713/236440436-c376f680-7c3f-4fc4-9156-4ab960173ea7.png)


- Row and column guesses: If the user enters non-numeric input, input outside the grid size, or guesses a location they have already tried, the game will display an error message and prompt the user to enter valid row and column coordinates.

![Screenshot (45)](https://user-images.githubusercontent.com/127791713/236439667-c1f4577d-e03c-4e66-b6ab-60bf9663db41.png)
![Screenshot (44)](https://user-images.githubusercontent.com/127791713/236438968-ecbac53f-2923-4364-adea-e82333cc802a.png)

### Implementation
- The error handling is implemented using "try-except" blocks and "while" loops in the code. This ensures that the game will continue to ask for valid input until the user provides it, preventing the game from crashing or entering an undefined state due to incorrect user input.


## Features
- Customizable grid size (3 to 15)
- Customizable number of ships (1 to the grid size)
- Display of player and computer boards with relevant symbols
- Randomized ship placement for both player and computer
- User input for row and column guesses
- Randomized computer guesses
- Hit and miss feedback for both player and computer
- Scoring and ship tracking
- Win/lose game result

![Screenshot (46)](https://user-images.githubusercontent.com/127791713/236439403-f43ad1e2-77c7-4483-a45d-dfcf655474a9.png)
![Screenshot (47)](https://user-images.githubusercontent.com/127791713/236440674-6343b06a-c1ae-4877-8be8-7fc361338ce0.png)

## Symbols
- S: Ship
- X: Hit
- 0: User Miss on Computer's Grid
- #: Computer Hit

## Future features
- Player can choose position of the ships
- different size ships

## Data model 
- the data model consists of classes and functions that represent game elements and their interactions. The primary classes used are BaseBoard, PlayerBoard, and ComputerBoard. The game also has utility functions to handle user input and computer input.

### Classes
- BaseBoard: This is the base class for the game board, containing common properties and methods for both the player's and computer's boards. The class initializes the grid size, number of ships, creates the grid, and places the ships on the grid. It also contains a method to print the current state of the grid.

- PlayerBoard: This class is derived from the BaseBoard class and represents the player's board. It initializes the player's name and calls the parent constructor. The class also contains a method to display the player's board.

- ComputerBoard: This class is derived from the BaseBoard class and represents the computer's board. It contains a method to display the computer's board with ships hidden and a method to print the current state of the hidden grid.

### Utility Functions
- get_computer_input(grid_size): This function generates random row and column coordinates within the grid size for the computer's move.

- get_user_input(grid_size): This function prompts the user for row and column coordinates within the grid size. It includes error handling to ensure the input is valid.

### Game Data Flow
- The game's data model primarily flows through the main game loop, where the player and computer take turns interacting with their respective game boards. During each turn, the user input or computer input is used to update the state of the game boards. The game continues until either the user or the computer has no remaining ships.

## Validator and testing
- The code passed through PEP8 Python Validator And no error found.
- Given invalid inputs the game will display an appropriate error message and ask the user to try again.
- Tested in my local terminal and in the code Institute Haruku Terminal.

## Bugs
- No bugs found.

## Deployment

This project was deployed Using code Institute python-essentials-template.

#### Steps for deployment
- Fork or clone this repository.
- create new heroku account or if you already have one press to create a new app.
- Add name for your new app And choose the region Go to settings and add buildpacks `python` and `nodeJS` In that order.
- add a _Config Var_ called `PORT`. Set this to `8000`.
- Link the Heruku app to the repository
- Click the Deploy

## Credits 
- code Institute For the deployment terminal.
- Wikipedia for The Details of of the Battleships game.
