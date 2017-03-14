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
    return self

  def ride(self):
    print 'Riding'
    self.miles += 10
    return self

  def reverse(self):
    print 'Reversing'
    self.miles -= 5
    return self



Bike1=Bike(500, 20)
Bike2=Bike(50,10)
Bike3=Bike(100,0)

Bike1.ride().ride().ride().reverse().displayInfo()

Bike2.ride().ride().reverse().reverse().displayInfo()

Bike3.reverse().reverse().reverse().displayInfo()

