# Python Class and Objects 

class Person:
  name = "Harry"
  occupation = "Programmer"
  netWorth = 100
  age = 24
  def info(self): # self is a reference to the current instance of the class
    print(f"Name: {self.name}")
    print(f"Occupation: {self.occupation}")
    print(f"Net Worth: {self.netWorth}")
    print(f"Age: {self.age}")

a = Person()
a.name = "Shubham"
a.occupation = "Doctor"

print(a.name,a.occupation,a.netWorth,a.age)
a.info()
b = Person()
b.info()