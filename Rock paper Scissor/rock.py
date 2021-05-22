import random
choices =["rock","paper","scissor"]

player1 = " "

while player1 not in choices:
    player1 =input("'rock' 'paper' 'scissor'??").lower()

player2 = random.choice(choices)

print(f"player1 : {player1}")
print(f"player2 : {player2}")   

if player1 == player2:
    print("Tie!!")

elif player1 == "rock":
    if(player2=="paper"):
        print("You Lose!!")
    else:
        print("You Won!!") 

elif player1 == "paper":
    if(player2 =="rock"):
        print("You Won!!")
    else:
        print("You Lose!!")

elif player1 =="scissor":
    if(player2=="paper"):
        print("You Won!!")
    else:
        print("You Lose!!")




