import random
class Car(object):
  def __init__(self, price, speed, fuel, mileage):
    print 'New Car'
    
    self.price= price
    self.speed= str(speed)
    self.fuel= str(fuel)
    self.mileage=str(mileage)
    
    self.tax='12%'
    if self.price > 10000:
      self.tax='15%'

  

  def display_all(self):
    print 'Price:', self.price 
    print 'Speed:', self.speed
    print 'Fuel:', self.fuel
    print 'Mileage:', self.mileage
    print 'Tax:', self.tax

Car1=Car(2000, '35mph', 'full', '15mpg')
Car2=Car(2000, '5mph', 'not full', '105mpg')
Car3=Car(2000, '15mph', 'kind of full', '95mpg')
Car4=Car(2000, '25mph', 'full', '25mpg')
Car5=Car(2000, '45mph', 'empty', '25mpg')
Car6=Car(2000000, '35mph', 'empty', '15mpg')



Car1.display_all()
Car2.display_all()
Car3.display_all()
Car4.display_all()
Car5.display_all()
Car6.display_all()




