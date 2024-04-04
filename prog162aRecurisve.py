#prog162aRecursive.py
import sys
sys.setrecursionlimit(5000)


def factLoop(n):
  product = 1
  for num in range(n, 0, 1):
    product *= num
  return product


def fact(n):
  if n == 1: return n
  return n * fact(n-1)

def main():
  num = int(input("Enter a number: "))
  while num != 0:
    factn = fact(num)
    print (f"{num}! = {factn}")
    num = int(input("enter a number: "))


if __name__ == "__main__":
  main()
  