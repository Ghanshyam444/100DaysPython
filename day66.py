# Difference between instances and classes
# Instances are created from classes
# Classes are created from instances
# Classes are objects
# Instances are not objects

class Employee:
  companyName = "Google" # class variable
  noOfEmployees = 0 # class variable
  def __init__(self, name):
    self.name = name # instance variable
    self.raise_amount = 0.02 # instance variable
    Employee.noOfEmployees += 1 # class variable
  def show(self):
    print(f"Name of the employee {self.name} and raise amount in {self.companyName} is {self.raise_amount} and number of employees is {self.noOfEmployees}")
    
# Employee.show(emp1)
emp1 = Employee("John")
emp1.raise_amount = 0.05
emp1.show()
Employee.companyName = "Microsoft"
emp2 = Employee("Jane")
emp2.companyName = "Facebook"
emp2.show()
emp1.show()
