from collections.abc import Mapping
from CL702q import*

def main():
  try:
    vehicles = []
    with open("Langdat/prog702q.txt", 'r') as f:
      num = int(f.readline())
      while num != 99:
        name = f.readline()
        tire = f.readline()
        if num == 1:
          worth = float(f.readline())
          p = Car(name, tire, worth)
          vehicles.append(p)
        elif num == 2:
          Mileage = int(f.readline())
          p = Truck(name, tire, Mileage)
          vehicles.append(p)
        elif num == 3:
          HomeT = f.readline().strip()
          p = Bus(name, tire, HomeT)
          vehicles.append(p)
        num = int(f.readline())
      totVeh = 0
      carWor = 0
      vehWor = 0
      large = ""
      truPoor = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
      tirTot = 0
      for vehicle in vehicles:
        if isinstance(vehicle, Car):
          worth = vehicle.worth
          tires = vehicle._tire
          totVeh += 1
          carWor += int(worth)
          vehWor += int(worth)
          tirTot += int(tires)
        elif isinstance(vehicle, Truck):
          mileage = vehicle.miles
          tires = vehicle._tire
          totVeh += 1
          TruckWorth = 50000 - (0.25 * int(mileage))
          if float(TruckWorth) < int(truPoor):
            truPoor = TruckWorth
          vehWor += TruckWorth
          tirTot += int(tires)
        elif isinstance(vehicle, Bus):
          Home = vehicle.city
          tires = vehicle._tire
          totVeh += 1
          if len(Home) > len(large):
            large = Home
          tirTot += int(tires)
      print("Total number of Vehicles:", totVeh)
      print("Total worth of Cars: $", carWor)
      print("Total worth of Vehicles: $", vehWor)
      print("Largest town name:", large)
      print("Least valued truck:", truPoor)
      print("Total number of Tires:", tirTot)
  except Exception as e:
    print("Error:", e)
  pass



if __name__ == "__main__":
  main()
