# dir, __dict__, help 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.version = 1.0

  
x = [1, 2, 3]
print(dir(x))
print(x.__add__)

p = Person("John", 36)
print(p.__dict__)

print(help(Person))

