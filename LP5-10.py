num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Second Number: "))
while (num2 > 0):
  temp = num1 % num2
  num1 = num2
  num2 = temp
print("Your Greatest Common Divisor = " + str(num1))