# using Class methods as alternative constructors

class Employee:
  def __init__ (self,name,salary):
    self.name = name
    self.salary = salary
    
  @classmethod
  def from_string(cls,string):
    name,salary = string.split("-")
    return cls(name,int(salary))
  
e = Employee("John",1000)
print(e.name)
print(e.salary)
# if input to be taken as string = "Harry-1000" and we want to split it into name and salary
string = "Harry-1200"
#e = Employee(string.split("-")[0],string.split("-")[1])
e1 = Employee.from_string(string)
print(e1.name)
print(e1.salary)