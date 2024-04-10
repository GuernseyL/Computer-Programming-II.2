# CL213f.py
class CL213f:
  def __init__(self, kwh):
    self.kwh = kwh
    self.cost = 0.0

  def calc(self):
    if self.kwh >= 0 and self.kwh <= 2000:
      bill = self.kwh * 0.07
    elif self.kwh > 2000 and self.kwh <= 10000:
      bill = self.kwh * 0.05
    elif self.kwh > 10000:
      bill = self.kwh * 0.04
    elif self.kwh < 0:
      bill = "Negative energy usage is not possible"
    pass

  def __str__(self):
    return f"The cost of {self.kwh} is "
    