from replit import clear

def winner_bid():
    up_bid = 0
    winner = ""
    for i in bides:
        bid_value = bides[i]
        if bid_value>up_bid:
            up_bid = bid_value
            winner = i
    print(f"The winner is {winner} and the bid was ${up_bid}")

print("***** Welcome to the bid program ********")
repeat = input("Do you wanna bid? Yes or  No ")
repeat = repeat.lower()
bides = {}
while repeat == "yes":
    name = input("What is you name? ")
    bid = float(input("What is you bid?  $"))
    bides[name]=bid
    repeat = input("Do you wanna do other bid? ")
    repeat = repeat.lower()
    if repeat == "yes":
        clear()


winner_bid()


