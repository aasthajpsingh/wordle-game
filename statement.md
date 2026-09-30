# Problem Statement

## Problem
Word-guessing games are usually played on websites that need an internet connection. Beginners learning Python have few small, readable programs that show how loops, conditions, string handling, input validation and time measurement work together in a real game.

## Project
**Wordle (terminal version)** is a command-line word-guessing game written in Python. The player chooses a difficulty level and gets 6 attempts to guess a hidden 5-letter word. After every guess, each letter is marked to show whether it is in the right place, in the wrong place, or not in the word.

## Scope
**In scope**
- Four difficulty levels (Easy, Medium, Hard, Expert), each with its own secret word
- Validation of guesses (must be exactly 5 letters, letters only)
- Letter-by-letter feedback after every guess
- Limit of 6 guesses per game
- Win / lose messages
- Timing of how long the player took

**Out of scope**
- Graphical or web interface
- Multiplayer or user accounts
- Checking guesses against a full English dictionary

## Target Users
- Students and casual players who want a quick word game in the terminal
- Beginners who want a simple example of a Python console program

## High-Level Features
1. **Difficulty selection** - menu with four levels
2. **Gameplay and feedback** - 6 guesses, CAPITAL letter = right letter right place, lowercase letter = right letter wrong place, `_` = letter not in word
3. **Input validation** - rejects guesses that are not 5 letters or contain non-letters (an invalid guess does not use up an attempt)
4. **Timer** - shows the time taken at the end of the game
