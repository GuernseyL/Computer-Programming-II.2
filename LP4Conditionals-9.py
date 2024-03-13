import random

PlayerNum = int(input("Please enter a number between 1 and 20: "))
ComputerNum = random.randint(1, 20)
print("Computer Number is: " + str(ComputerNum))
print("Player Number is: " + str(PlayerNum))
if PlayerNum == ComputerNum:
  print("You Win!")
else:
  print("You Lost!")