import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]
# Choosing random word from list
word_list = ["blobfish", "platypus", "shoebill", "baboon"]
chosen_word = random.choice(word_list)

# Creating a variable that indicates that the game has not ended
end_of_game = False

# Creating a variable called 'lives' to keep track of the number of lives left.
lives = 6

# For testing
print(f'The answer is {chosen_word}.')

# Created an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
display = []
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
    if guess not in chosen_word:
        lives -= 1

    # Join all the elements in the list and turn it into a String. So it comes as a string is display.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # printing the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if lives == 0:
        # To end the while loop setting the end_of_game variable to true
        end_of_game = True
        print("You lose.")
