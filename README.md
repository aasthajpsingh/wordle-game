# Wordle (Terminal Game)

## Overview
A command-line Wordle game written in Python. Choose a difficulty level and try to guess the hidden 5-letter word in 6 attempts. After each guess, every letter is marked so you can narrow down the answer.

## Features
- 4 difficulty levels: Easy, Medium, Hard, Expert
- 6 guesses per game
- Letter-by-letter feedback after every guess
- Input validation (exactly 5 letters, letters only)
- Win and "Game Over" messages (the correct word is revealed on a loss)
- Timer that shows how many seconds the game took

## How to Read the Feedback
| Mark | Meaning |
|------|---------|
| `A` (CAPITAL letter) | right letter, right position |
| `a` (lowercase letter) | right letter, wrong position |
| `_` | letter is not in the word |

Example (secret word `BRAID`, guess `crane`): output `_RA__` - R and A are in the correct places; C, N and E are not in the word.

## Technologies Used
- Python 3 (standard library only: `sys`, `string`, `datetime`)
- Git and GitHub for version control
- VS Code as the editor

## Steps to Install & Run
1. Install Python 3 from https://www.python.org/downloads/
2. Download this repository (green **Code** button -> **Download ZIP**) and unzip it, or clone it:
   `git clone https://github.com/<your-username>/<repo-name>.git`
3. Open a terminal in the project folder and run:
   ```
   python wordle.py
   ```
   (use `python3 wordle.py` on macOS/Linux)
4. Enter a level number (1 to 4) and start guessing.

No extra packages are required.

## Instructions for Testing
The program is tested manually by running it and checking the following cases:

| # | Test | Input | Expected result |
|---|------|-------|-----------------|
| 1 | Winning on Easy | level `1`, guess `chill` | Prints `CHILL`, then `WORD GUESSED!` and the time taken |
| 2 | Wrong guess | level `2`, guess `crane` | Prints `_RA__`, then `TRY AGAIN`; guesses left goes down by 1 |
| 3 | Too short / too long | guess `cat` | `Please enter a 5-letter word!`; guesses left does not change |
| 4 | Non-letters | guess `ab3de` | `Letters only please!`; guesses left does not change |
| 5 | Losing | 6 wrong guesses | `Game Over! The word was: ...` |
| 6 | Invalid level | level `9` | `Invalid Input. Please Try Again` and the program exits |
| 7 | Timer | finish any game | `Time taken: N seconds` is printed |

## Author
Aastha Singh- 26MEI10003
