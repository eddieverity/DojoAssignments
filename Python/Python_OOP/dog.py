from animal import Animal
class Dog(Animal):
  def __init__(self):
   
    self.health=150
    

  def pet(self):
    self.health+=5
    return self

dog1=Dog('dog')
dog1.walk().walk().walk().run().run().pet().displayHealth()