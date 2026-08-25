import random

print("1 - rock")
print("2 - paper")
print("3 - scissor")

print("player1,select your choice")
player1 = int(input())
print("player2,select your choice")
player2 = int(input())

comp = random.randint(1,3)
print("computer choice is",comp)

if player1 == 1 and player2 == 3 or player1 == 2 and player2 == 1 or player2 == 3 and player2 == 2 :
    print("player1 is the winner")
    if player1 == 3 and player2 == 1 or player1 == 1 and player2 == 2 or player1 == 2 and player2 == 3 :
        print("player2 is the winner")
        if player1 == player2 :
            print("its a tie")