import random
import hangman_words
import hangman_art

# Updating the word list to use the 'word_list' from hangman_words.py
# Choosing random word from list
# Deleted this - word_list = ["blobfish", "platypus", "shoebill", "baboon"]
chosen_word = random.choice(hangman_words.word_list)

# Creating a variable that indicates that the game has not ended
end_of_game = False

# Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

# Importing the logo from hangman_art.py to print it at the start of the game.
print(hangman_art.logo)

# For code testing
# print(f"Pssst, the solution is {chosen_word}.")

# Created an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
display = []
guessed = []
for letter in chosen_word:
    display.append('_')

while not end_of_game:
    # Asking the user for a letter
    guess = input("Guess a letter: ").lower()

    # Looping through each position in the chosen_word
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    position = -1
    for letter in chosen_word:
        position += 1
        if letter == guess:
            display[position] = letter
    # OR
    # for position in range(len(chosen_word)):
    #   letter = chosen_word[position]

    # If guess is not a letter in the chosen_word,then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop, and it should print "You lose."
    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess not in chosen_word:
        print(f"{guess} is not in the word.")
        if guess not in guessed:
            lives -= 1
            if lives == 0:
                # To end the while loop setting the end_of_game variable to true
                end_of_game = True
                print(f"This was the word: {chosen_word}")
                print("You lose")

    # If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess not in guessed:
        guessed.append(guess)
        # print(guessed)
    else:
        print(f"You have already guessed letter {guess}.")

    # Join all the elements in the list and turn it into a String. So it comes as a string is display.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

# Importing the stages from hangman_art.py
    print(hangman_art.stages[lives])
