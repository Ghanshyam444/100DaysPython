class Employee:
  company = "Google"
  def show(self):
    print(f"The name is {self.name} and the company is {self.company}")
   
  @classmethod # class method decorator means this method is bound to the class and not the instance of the class 
  def changeCompany(cls,company):
    cls.company = company 
  
  
e1 = Employee()
e1.name = "John"
e1.show()
e1.changeCompany("Microsoft")
e1.show()
print(Employee.company)