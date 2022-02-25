import random
logo = ''' 
██████╗ ██╗   ██╗███████╗███████╗███████╗     █████╗     ███╗   ██╗██╗   ██╗███╗   ███╗███████╗██████╗ ███████╗██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ██╔══██╗    ████╗  ██║██║   ██║████╗ ████║██╔════╝██╔══██╗██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗    ███████║    ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║    ██╔══██║    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║    ██║  ██║    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██████╔╝███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                        '''
print(logo)
print("Welcome to the number guessing game! \n I'm thinking of a number between 1 and 100 ")

# create the variables that will memory our values
number = 0
numbers = []
guess = 0
for i in range(1, 100):
    number = i
    numbers.append(number)
# selecting our number
number = random.choice(numbers)
# choose the level
level = input("Do you want play in the 'easy' game or 'hard' game? : ")
lifes = 0
if level == "easy":
    lifes = 10
elif level == "hard":
    lifes = 5
# game function
while guess != number and lifes > 0:
    guess = int(input(" Type your guess : "))
    lifes -= 1
    if guess > number and lifes > 0:
        print(f"Too high!! You kick was {guess} , remains {lifes} attempts ")
    elif guess < number and lifes > 0:
        print(f"To low !! You kick was {guess} , remains {lifes} attempts ")
if guess == number:
    print(f"You win , the right number was {number} ")
if guess != number:
    print(f"You lose! the right number was {number}")
