# Constructors
# Python has a number of built-in constructors that can be used to create new objects.
class Person:
  def __init__(self,name,occupation,netWorth,age): # this is a constructor method which is called when a new object is created and returns None
    self.name = name
    self.occupation = occupation
    self.netWorth = netWorth
    self.age = age
  #name = "Harry"
  #occupation = "Programmer"
  #netWorth = 100
  age = 24
  def info(self):
    print(f"Name: {self.name}")
    print(f"Occupation: {self.occupation}")
    print(f"Net Worth: {self.netWorth}")
    print(f"Age: {self.age}")
    
a = Person("Harry","Programmer",100,24)
#a.info()
#a.name = "Divya"
#a.occupation = "HR"
a.info()
b = Person("Divya","HR",200,25)
b.info()

# c = Person() this will give an error as the constructor requires 4 arguments

