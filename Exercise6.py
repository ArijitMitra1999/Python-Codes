import random
User = int(input("Choose 1.stone, 2.paper or 3.seasor:\n "))
list = [1,2 ,3]
choice = random.choice(list)
print("Computer Choose : \n",choice)
#choice is a function of random
if User == choice : print("Match is Draw")

elif User== 1 and choice== 2 : print("You Lost the Game")

elif (User== 1 and choice== 3) : print("Congo! You Won the Game")

elif (User== 2 and choice == 3) : print("You Lost the Game")

elif (User== 2 and choice == 1) : print("Congo! You Won the Game")

elif (User== 3 and choice == 1) : print("You Lost the Game")

elif (User== 3 and choice == 2) : print("Congo! You Won the Game")
