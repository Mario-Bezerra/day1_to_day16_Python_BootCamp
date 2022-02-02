import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
moves = [rock,paper,scissors]
player_choosen = int(input(print(("What do you choose? 0 for ROCK , 1 for PAPER and 2 for SCISSORS "))))
print(moves[player_choosen])
print("Computer :\n")
computer = random.randint(0,2)
print(moves[computer])

if player_choosen==0 and computer==0:
    print("TIED")
elif player_choosen==0 and computer==1:
    print("YOU LOSE")
elif player_choosen==0 and computer==2:
    print("YOU WIN")
elif player_choosen==1 and computer==0:
    print("YOU WIN")
elif player_choosen==1 and computer==1:
    print("TIED")
elif player_choosen==1 and computer==2:
    print("YOU LOSE")
elif player_choosen==2 and computer==0:
    print("YOU LOSE")
elif player_choosen==2 and computer==1:
    print("YOU WIN")
elif player_choosen==2 and computer==2:
    print("TIED")

