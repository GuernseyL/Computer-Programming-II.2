Eggs = int(input("Enter the Amount of Eggs: "))
Extra = Eggs % 12
Dozen = Eggs // 12
if Eggs <= 0:
  print("You have not bought any eggs")
else:
  if Dozen > 0 and Dozen < 4:
    priceA = 0.5
  elif Dozen >= 4 and Dozen < 6:
    priceA = 0.45
  elif Dozen >= 6 and Dozen < 11:
    priceA = 0.4
  elif Dozen >= 11:
    priceA = 0.35
CostA = Dozen * priceA
priceB = priceA/12
CostB = Extra * priceB
TotalCost = CostA + CostB
print("You have bought " + str(Dozen) + " Dozen and " + str(Extra) + " Extra Eggs Coming to a total cost of $" + str(round(TotalCost, 2)))