# Static methods
# Static methods are methods that are bound to a class rather than its object. They do not require a class instance creation. So, they are not dependent on the state of the object.

class Math:
  def __init__(self,num):
    self.num = num
    
  def addtonum(self,num2):
    self.num += num2

  @staticmethod
  def add(num1,num2):
    return num1 + num2

# result = Math.add(1,2)
# print(result) # output: 3
a = Math(5)
print(a.num)
a.addtonum(5)
print(a.num)

print(Math.add(1,2)) # output: 3
