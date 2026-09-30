
import sys             # import sys so we can exit the program on invalid input
import string           # import string to get the list of lowercase letters for validation
from datetime import datetime           # import datetime to measure how long the player takes

word1 = "CHILL"
word2 = "BRAID"
word3 = "QUIET"
word4 = "TORSE"


def game(word):
    count = 6

    # keep looping until the player runs out of guesses
    while count > 0:
        guess = input(f"Enter guess ({count} guesses left): ").lower()

        # reject guesses that are not 5 letters long
        if len(guess) != 5:
            print("Please enter a 5-letter word!\n")
            continue

        valid = True

        # check that every character is a letter from a to z
        for ch in guess:
            if ch not in string.ascii_lowercase:
                valid = False

        if valid == False:
            print("Letters only please!\n")
            continue
        
        result = ""

        # compare each letter of the guess with the secret word
        for i in range(5):
            if guess[i] == word[i].lower():
                result += guess[i].upper()  
            elif guess[i] in word.lower():
                result += f"{guess[i]}"  
            else:
                result += "_"  
        
        print(result)

        # if the guess matches the word, the player wins and the function ends    
        if guess == word.lower():
            print("WORD GUESSED!")
            return
        
        count -= 1
        print("TRY AGAIN\n")
    
    # reaching here means all 6 guesses were used without winning
    print(f"Game Over! The word was: {word}")


# display the welcome banner and instructions
print("= " * 40)
print("                            WELCOME TO WORDLE!")
print("= " * 40)
print("\nHOW TO PLAY:")
print("1. Guess the hidden 5-letter word in 6 tries")
print("2. After every guess, each letter is marked:")
print("   CAPITAL LETTER = right letter, right position")
print("   letter       = right letter, wrong position")
print("   _              = letter not in the word\n")
print("3. Only 5-letter words are accepted\n")
print("= " * 40)
print("\nChoose the level of difficulty")
print("1. Easy")
print("2. Medium")
print("3. Hard")
print("4. Expert")
print("Enter a number")
n = int(input())

# record the start time just before the game begins
start = datetime.now()

if n == 1:
    game(word1)
elif n == 2:
    game(word2)
elif n == 3:
    game(word3)
elif n == 4:
    game(word4)

# any other number is invalid, so exit the program
else:
    print("Invalid Input. Please Try Again")
    sys.exit(0)

# record the end time and work out how long the game lasted
end = datetime.now()
taken = end - start
print("Time taken:", taken.seconds, "seconds")