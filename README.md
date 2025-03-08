# Hangman Game

## Introduction
This is a simple Hangman game implemented in Python. The game reads a list of words from a text file (`words.txt`) and selects a secret word based on a given index. The player must guess the word within a limited number of attempts (6 tries) before the Hangman figure is fully drawn.

## How to Play
1. Run the Python script.
2. Enter the path to the `words.txt` file when prompted.
3. Enter an index number to select a word from the file.
4. The game will display the Hangman ASCII art and the hidden word as underscores.
5. Guess one letter at a time.
   - If the letter is correct, it will be revealed in the word.
   - If the letter is incorrect, the Hangman figure progresses.
6. Win by guessing all letters in the word before running out of tries.
7. Lose if you reach 6 incorrect guesses before completing the word.

## Requirements
- Python 3.x
- `words.txt` file (included in the GitHub repository).

## Running the Game
To start the game, run:
```sh
python hangman.py
```

## Features
- Reads words from an external file.
- ASCII art representation of the Hangman.
- Input validation to prevent duplicate or invalid guesses.
- Displays previously guessed letters.
- Checks for a win or loss condition.

## File Descriptions
- `hangman.py`: The main game script.
- `words.txt`: A word list file included in the GitHub repository.

## Author
This Hangman game was implemented using Python and basic file handling techniques. Enjoy playing!

