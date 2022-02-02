import random
import replit


def card_player():
    card = random.choice(cards)
    player.append(card)
    return card


def card_dealer():
    card = random.choice(cards)
    dealer.append(card)
    return card


def game_result():
    if sum(dealer) > 21:
        print(f"Your cards = {player} \n Dealer card = {dealer}\n You Winnnn!!! The dealer exceeded Dealer = {sum(dealer)} your final score = {sum(player)} ")
    elif sum(player) > 21:
        print(f"Your cards = {player} \n Dealer card = {dealer}\n You exceeded and lose!! \n Dealer = {sum(dealer)} Player :  {sum(player)} ")
    elif sum(player) == 21:
        print(f"Your cards = {player} \n Dealer card = {dealer}\n You win!!! Player : {sum(player)} the dealer lost with {sum(dealer)}")
    elif sum(player) > sum(dealer):
        print(f"Your cards = {player} \n Dealer card = {dealer}\n You win the game!!! \n Player : {sum(player)} Dealer : {sum(dealer)} ")
    elif sum(dealer) < sum(player):
        print(f"Your cards = {player} \n Dealer card = {dealer}\n You lose the game!!! \n Player : {sum(player)} Dealer: {sum(dealer)} ")
    elif sum(dealer) == sum(player):
        print(f"Your cards = {player} \n Dealer card = {dealer}\n You and the dealer draw with Player: {sum(player)} Dealer: {sum(dealer)}")


repeat = input("Do you wanna play BlackJackPy ? Type 'y' for yes or 'n' for no : ")
card = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = []
dealer = []
while repeat == "y":
        player = []
        dealer = []
        card_player()
        card_player()
        card_dealer()
        print(f"Your cards are : {player} and you sum is {sum(player)}")
        print(f"The dealer card is {dealer}")
        card_dealer()
        if sum(player) == 21:
            hint_or_stand = "stand"
        else:
            hint_or_stand = "hint"

        while hint_or_stand == "hint":
            hint_or_stand = input("Do you wanna hint or stand? ")
            if hint_or_stand == "hint":
                card_player()
                print(f"Your cards : {player} and your sum : {sum(player)}\n The dealer cards : {dealer} and the Dealer sum :{sum(dealer)}\n ")
            if sum(player) == 21:
                hint_or_stand = "stand"
            if sum(player)>21:
                hint_or_stand = "stand"
        hint_or_stand = "stand"
        if hint_or_stand == "stand":
            if sum(player) < 21 and sum(dealer) < 17:
                while sum(dealer)<17:
                    card_dealer()
                game_result()
                repeat = input("Do you wanna play BlackJackPy again ? Type 'y' for yes or 'n' for no")

            else:
                game_result()
                repeat = input("Do you wanna play BlackJackPy again ? Type 'y' for yes or 'n' for no")
