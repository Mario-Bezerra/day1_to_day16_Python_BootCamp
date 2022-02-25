from game_data import data
from logo import logo
from logo import vs
import random
import replit

#variaveis importantes para rodar
repeat = 1
score = 0
person1 = random.choice(data)
person2 = random.choice(data)
#if para verificar se a pessoa 1 é igual a pessoa 2
if person1==person2:
    person2=random.choice(data)
#função do jogo
while repeat == 1:
    print(f"Compare A : {person1['name']} , a {person1['description']},from {person1['country']} ")
    print(vs)
    print(f"Compare B : {person2['name']} , a {person2['description']},from {person2['country']} ")
    asnwer = input("Who has more followers ? Type 'A' or 'B' : ")
    if asnwer == "A":
        #checando a resposta
        if person1['follower_count']>person2['follower_count']:
            score+=1
            repeat = 1
            person1 = person2
            person2 = random.choice(data)
            if person1 == person2:
                person2 = random.choice(data)
            print(f"You are right! Current score {score}")
        #finalizando se estiver errado
        else:
            print(f"Wrong choice , your score was {score}")
            repeat = 0
    if asnwer == "B":
        if person2['follower_count']>person1['follower_count']:
            score+=1
            repeat = 1
            person1 = person2
            person2 = random.choice(data)
            if person1 == person2:
                person2 = random.choice(data)
            print(f"You are right! Current score {score}")
        else:
            print(f"Wrong choice , your score was {score}")
            repeat = 0



