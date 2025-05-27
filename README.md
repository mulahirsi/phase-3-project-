# Python CLI Tic Tac Toe

## Description
A command-line interface Tic Tac Toe game built with Python. Players can take turns marking X's and O's on a 3x3 grid.

## Features
- 3x3 game board
- Two player gameplay
- Command line interface
- Input validation
- Win/Draw detection

## Installation
```bash
# Clone the repository
git clone <repository-url>

# Navigate to project directory
cd tic-tac-toe

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate
```

## Usage
```bash
# Run the game
python src/main.py
```

## Project Structure
```
.
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── game/
│   │   ├── __init__.py
│   │   ├── board.py
│   │   └── player.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
└── tests/
    ├── __init__.py
    ├── test_board.py
    └── test_player.py
```
