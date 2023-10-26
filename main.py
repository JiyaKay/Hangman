import hangman_words
import hangman_art
import random

# Updating the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Importing the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

# Testing code
print(f'Pssst, the answer is {chosen_word}.')

# Creating blanks
display = []
guessed = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Checking if user is wrong.
    # If the letter is not in the chosen_word, print out the letter and let the player know it's not in the word.
    if guess not in chosen_word:
        print(f"{guess} is not in the word.")
        if guess not in guessed:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose")

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess not in guessed:
        guessed.append(guess)
        print(guessed)
    else:
        print(f"You have already guessed letter {guess}.")

    # Joining all the elements in the list and turning it into a String.
    print(f"{' '.join(display)}")

    # Checking if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Importing the stages from hangman_art.py.
    print(hangman_art.stages[lives])
