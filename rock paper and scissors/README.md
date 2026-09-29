# Rock Paper Scissors

A Python-based Rock Paper Scissors game developed using modular programming. The game allows the player to compete against the computer, view the scoreboard, check game history, and access the game rules through an interactive menu.

## Features

- Play Rock Paper Scissors against the computer
- Random computer move generation
- Display wins, losses, draws, total games, and win percentage
- Save and display game history
- Interactive rules section
- Input validation for player choices
- Unit tests for game-winning logic

## Technologies Used

- Python
- Random module
- File handling
- Object-oriented programming
- Unit testing with `unittest`

## Project Structure

```text
rock paper and scissors/
│
├── main.py              # Main program and menu
├── game.py              # Determines the game result
├── computer.py          # Generates computer choices
├── utils.py             # Gets and validates player input
├── scoreboard.py        # Manages scores and statistics
├── history.py           # Saves and displays game history
├── test_game.py         # Unit tests for game logic
└── data/
    └── game_history.txt # Stores previous game results
```

## How to Run

1. Make sure Python is installed on your computer.
2. Open the project folder in a terminal or command prompt.
3. Run:

```bash
python main.py
```

4. Select an option from the menu and follow the instructions.

## Running Tests

To run the unit tests, use:

```bash
python -m unittest test_game.py
```

## Game Rules

- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.
- If both choices are the same, the result is a Draw.

## Purpose

This project demonstrates the use of Python fundamentals, modular programming, functions, classes, file handling, user input, and unit testing through a simple interactive game.
