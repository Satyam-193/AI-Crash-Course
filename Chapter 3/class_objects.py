
class Car:

  def __init__(self, vmax, acc):
    self.vmax = vmax
    self.acc = acc
  
  def time(self, vcc):
    t = (self.vmax -vcc) /self.acc
    return t

car = Car(5, 3)
time = car.time(2)
print(time)
