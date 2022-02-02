import random
from replit import clear
import word_list
stages = ['''
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
=========''', '''
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
''']

end_of_game = False
chosen_word = random.choice(word_list.word_list)
word_length = len(chosen_word)
error = 6

display = []
for _ in range(word_length):
    display += "_"
from word_list import logo
print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        error -= 1
        if error == 0:
            end_of_game = True
            print("You lose the game")
    print(stages[error])

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")