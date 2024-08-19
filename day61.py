# Inheritance in Python
# Inheritance is a mechanism in which one class acquires the property of another class. For example, a child inherits the traits of his/her parents. With inheritance, we can reuse the fields and methods of the existing class.

class Employee:
  def __init__(self,name,id):
    self.name = name
    self.id = id
    
  def show(self):
    print(f"Name: {self.name}")
    print(f"IDs: {self.id}")
    
class Programmer(Employee):
  def __init__(self,name,id,language):
    super().__init__(name,id)
    self.language = language
    
  def show(self):
    super().show()
    print(f"Language: {self.language}")
    
e1 = Employee("Harry",100)
e1.show()

e2 = Programmer("Divya",200,"Python")
e2.show()

