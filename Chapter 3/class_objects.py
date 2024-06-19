
class Car:

  def __init__(self, vmax, vc, acc):
    self.vmax = vmax
    self.vc = vc
    self.acc = acc
  
  def time(self, vm, vcc, ac):
    time = (vm -vcc) /ac
    print(time)

car = Car(5, 2, 3)
car.time(5, 2, 3)
