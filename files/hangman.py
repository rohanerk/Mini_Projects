# Objective of Hangman
# A. Limited no of wrong guesses
# B. Each correct guess reveals the letter in its position(s)
# C. Each wrong guess brings you closer to losing

# Choose a secret word

import random

words = ['apple','bread','chair','plant']
word = random.choice(words)

# Setup the Game State

guessed_letters = []
tries_left = 6
display = ["_"]*len(word)

# Game loop

while tries_left > 0 and "_" in display:
    print("Word:"," ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        print("Wrong")
        tries_left -= 1
        print(f"Tries left: {tries_left}")

# End the Game

if "_" not in display:
    print("You won the game")

else:
    print("You lost.")
