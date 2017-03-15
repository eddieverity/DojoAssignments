from animal import Animal
class Dragon(Animal):
  def __init__(self, name):

    super(Dragon, self).__init__(name)
    self.health=170
 
    super(Dragon, self).displayHealth()
    print "I'm a dragon!"

  def fly(self):
    self.health-=10
    return self

dragon1=Dragon('dragon')
dragon1.walk().walk().walk().fly().fly().displayHealth()