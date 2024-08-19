# method Overriding
# Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already provided by its parent class.

class shape:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    
  def area(self):
    return self.x * self.y
  
class circle(shape):
  def __init__(self,r):
    self.r = r
    super().__init__(r,r)
    
  def area(self):
    return 3.14 * super().area()
  
rec = shape(10,20)
print(rec.area())

c = circle(10)
print(c.area())