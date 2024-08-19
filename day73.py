# Dunder or Magic Methods in Python
# Dunder or Magic methods in Python are the special methods that have double underscores at the beginning and end of their names.
# They are used to create functionality that can't be represented as a normal method.

class Employee:
  def __init__ (self,name):
    self.name = name
  def __len__(self):
    i = 0
    for c in self.name:
      i += 1
    return i
  def __str__(self): # str is used to print the object in string format
    return f"Name of the employee is {self.name} str\t"
  
  def __repr__(self): # repr is used to print the object in string format but it is used for debugging and development purpose and executes when str falls back
    return f"Name of the Employee is {self.name} repr\t"
  
  def __call__(self):
    print(f"{self.name} is a good employee")