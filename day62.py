# There are no public, protected, or private keywords in Python classes.

# Access modifiers are used to restrict the access of a class, methods, and variables in Python.

# By default, all the attributes and methods of a class are public.

# for private attributes and methods, we use double underscore __ before the attribute or method name.
class Employee:
  def __init__(self,):
    self.__name = "harry" # private variable
   
a = Employee()
# print(a.__name) cannot be accessed directly as it is a private variable
print(a._Employee__name) # this is a way to access the private variable called as name mangling

print(a.__dir__()) # this will show all the attributes of the object

# for protected attributes and methods, we use a single underscore _ before the attribute or method name.
# Example:
class Employee:
  def __init__(self):
    self._name = "harry" # protected variable

a = Employee()
print(a._name) # this is a way to access the protected variable
