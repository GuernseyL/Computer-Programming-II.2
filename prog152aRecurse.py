#prog152aRecursive.py
import sys
sys.setrecursionlimit(5000)

def Sum(n):
  if n <= 1: return n
  return n + Sum(n-3)

def main():
  num = int(input("Enter a number: "))
  while num != 0:
    sumn = Sum(num)
    print ("Sum Series = " + f"{sumn}")
    num = int(input("enter a number: "))

if __name__ == "__main__":
  main()