# Wordle Game

Wordle Game is a simple Python-based word guessing game where the player has to guess a 5-letter word within 6 attempts. The words are fetched from an API, and feedback is provided for each guess.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python installed on your system
- `requests` module installed for Python
- Internet connection to access the words API

### Installing

- Clone this repository to your local machine
- Navigate to the cloned folder through terminal
- Run `wordle.py` using Python

```bash
python wordle.py
```

### Usage

- The game fetches a list of 5-letter words from an API and selects a random word as the solution.
- The player must guess the correct word within 6 attempts.
- After each guess, feedback is provided indicating correct and misplaced letters.

### Game Rules

- Each guess must be a 5-letter word.
- The game is case-insensitive.
- Feedback symbols:
  - Correct letters in correct positions are displayed as the letters themselves.
  - Correct letters in wrong positions are indicated with a '?' symbol.
  - Incorrect letters are shown as '_'.
