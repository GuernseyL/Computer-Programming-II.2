#CL701g.py
class Vehicle:
  def __init__(self, name, tire):
    self._name = name
    self._tire = tire

  def getName(self):
    return self._name


class Car(Vehicle):
  def __init__(self, name, tire, Money):
    super().__init__(name, tire) # or Person.__init__(fn, ln)
    self.worth = Money

class Truck(Vehicle):
  def __init__(self, name, tire, Mileage):
    super().__init__(name, tire)
    self.miles = Mileage


class Bus(Vehicle):
  def __init__(self, fn, ln, HomeT):
    super().__init__(fn, ln)
    self.city = HomeT
