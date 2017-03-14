import random
class Bike(object):
  def __init__(self, price, max_speed):
    print 'New Bike'
    self.miles=0
    self.price=price
    self.max_speed=max_speed

  def displayInfo(self):
    print 'Price:', self.price 
    print 'Maximum speed:', self.max_speed
    print 'Miles:', self.miles

  def ride(self):
    print 'Riding'
    self.miles += 10

  def reverse(self):
    print 'Reversing'
    self.miles -= 5



Bike1=Bike(500, 20)
Bike2=Bike(50,10)
Bike3=Bike(100,0)

Bike1.ride()
Bike1.ride()
Bike1.ride()
Bike1.reverse()
Bike1.displayInfo()

Bike2.ride()
Bike2.ride()
Bike2.reverse()
Bike2.reverse()
Bike1.displayInfo()

Bike3.reverse()
Bike3.reverse()
Bike3.reverse()
Bike3.displayInfo()
