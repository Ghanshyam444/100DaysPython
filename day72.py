# Super Keyword
# Super() is a built-in method that allows access to methods and properties of a parent or sibling class.
# It is used to call the constructor of the parent class and to access the parent class's methods and properties.

#class ParentClass:
#  def parent_method(self):
#    print("This is the parent method")
    
#class ChildClass(ParentClass):
#  def parent_method(self):
#    print("hello  harry")
#    super().parent_method()
#  def child_method(self):
#    print("This is the child method")
#    super().parent_method()
    
#child_object = ChildClass()
#child_object.child_method()
#child_object.parent_method()

class Employee:
  def __init__ (self,name,id):
    self.name = name
    self.id = id
  
class Programmer(Employee):
  def __init__ (self,name,id,lang):
    super().__init__(name,id)
    self.lang = lang
    
rohan = Employee("Rohan",1)
harry = Programmer("Harry",2,"Python")
print(rohan.name)
print(harry.name)
print(harry.lang)
print(harry.id)