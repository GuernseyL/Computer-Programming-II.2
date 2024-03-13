class LP3:
  def __init__(self, design, code, debug, test):
    self.design = design
    self.code = code
    self.debug = debug
    self.test = test

  def timecalc(self):
    self.total = self.design + self.code + self.debug + self.test
    self._tdes = round(self.design / self.total * 100, 3)
    self._tcod = round(self.code / self.total * 100, 3)
    self._tdeb = round(self.debug / self.total * 100, 3)
    self._ttes = round(self.test / self.total * 100, 3)

  def getdes(self):
    return str(self._tdes) + "%"

  def getcod(self):
    return str(self._tcod) + "%"

  def getdeb(self):
    return str(self._tdeb) + "%"

  def gettes(self):
    return str(self._ttes) + "%"
    
def main():
  des = int(input("Enter design time:"))
  cod = int(input("Enter coding time:"))
  deb = int(input("Enter debuging time:"))
  tes = int(input("Enter testing time:"))
  Lp = LP3(des, cod, deb, tes)
  Lp.timecalc()
  print("Time" + "  " + "% Time")
  print("Designing" + "  " + Lp.getdes())
  print("Coding" + "  " + Lp.getcod())
  print("Debugging" + "  " + Lp.getdeb())
  print("Testing" + "  " + Lp.gettes())
  pass


if __name__ == "__main__":
  main()