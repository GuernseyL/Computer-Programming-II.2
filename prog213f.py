# Prog 213f.py
from CL213f import *


def main():
  try:
    elechills = []
    with open("Langdat\prog213f.dat", 'r') as f:
      for line in f:
        kwh = int(line)
        if kwh != -999:
          bill = CL213f(kwh)
          elecbills.append(bill)
    for bill in elecbills:
      bill.calc()
      print(bill)
  except Exception as e:
    print("Error:", e)
  pass


if __name__ == "__main__":
  main()