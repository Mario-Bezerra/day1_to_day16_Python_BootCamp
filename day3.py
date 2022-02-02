print("Welcome to the treasure island .\n Your mission is find the treasure")
side=input(print('Choose "left" or "right"'))
if side =="right" or side!="left":
  print("End game. You'r dead")
else:
  act=input(print('Do you wanna "swim" or "wait"'))
  if act=="swim" or act!="wait":
    print("Attacked by trout\n GAME OVER")
  else:
    door=input(print('Wich door ? "blue" , "red" or "yellow?"'))
    if door=="red":
      print("Burned by fire \n GAME OVER")
    elif door=="blue":
      print("Eaten by beasts \n GAME OVER")
    elif door=="yellow":
      print("You win and are rich now")
    else :
      print("MISTAKE! \n GAME OVER")
