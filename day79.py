# Multiple Inheritance
# Multiple inheritance is a feature in which a class can inherit attributes and methods from more than one parent class.

class Employee:
  def __init__ (self,name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__ (self,dance):
    self.dance = dance
  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee,Dancer): 
  def __init__(self,name,dance):
    self.dance = dance
    self.name = name 
  
o = DancerEmployee("Harry","Break")
print(o)
print(o.dance)

# In the above example, the DancerEmployee class inherits from both the Employee and Dancer classes.
o.show()
# if we inherit as class DancerEmployee(Dancer,Employee): then the output will be:
# The dance is Break

print(DancerEmployee.mro()) # Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes.

