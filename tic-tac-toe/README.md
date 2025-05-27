# README.md for Tic Tac Toe Project

# Tic Tac Toe Game

## Description
A command-line interface implementation of the classic Tic Tac Toe game. Players can take turns to place their symbols on the board, and the game checks for win conditions after each move.

## Installation
```bash
# Clone the repository
git clone <repository-url>

# Navigate to project directory
cd tic-tac-toe

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
# Run the game
python src/main.py
```

## Project Structure
```
tic-tac-toe
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── game
│   │   ├── __init__.py
│   │   ├── board.py
│   │   └── player.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── tests
│   ├── __init__.py
│   ├── test_board.py
│   └── test_player.py
├── requirements.txt
├── setup.py
└── README.md
```