# Number Guesser Game

This is a Python-based number guessing game where the player tries to guess a randomly generated number within a specified range.

## Features

- The program generates a random number within a predefined range.
- The player inputs guesses, and the program provides feedback:
  - "Too high" if the guess is greater than the target number.
  - "Too low" if the guess is less than the target number.
  - "Correct" when the guess matches the target number.
- Tracks the number of attempts made by the player.

## How to Play

1. Run the script using Python.
2. The program will prompt you to guess a number.
3. Enter your guesses until you find the correct number.

### Example

```bash
Guess a number between 1 and 100: 50
Too high!
Guess a number between 1 and 100: 25
Too low!
Guess a number between 1 and 100: 30
Correct! You guessed the number in 3 attempts.
```

## Requirements

- Python 3.x

## How It Works

The game uses Python's `random` module to generate a random number. It then enters a loop where the player inputs guesses, and the program provides feedback until the correct number is guessed.

This project is a fun way to practice Python programming, including loops, conditionals, and user input handling.
