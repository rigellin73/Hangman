import random

from ascii_art import logo, stages
from dictionary import word_list

lives = 6
chosen_word = random.choice(word_list)
guessed_word = ["_"] * len(chosen_word)

print(logo)

game_over = False
guess = ""

while not game_over:
    print(f"Word to guess: {''.join(guessed_word)}")
    guess = input("Guess a letter: ").lower()
    guessed = False

    for index, letter in enumerate(chosen_word):
        if guess == letter:
            guessed = True
            guessed_word[index] = letter

    if not guessed:
        lives -= 1

    print(stages[lives])

    if lives == 0:
        game_over = True
        print("You lose =(")

    if not "_" in guessed_word:
        game_over = True
        print("You win =)")

print(f"The word was: {chosen_word}")
