# Opeartor Overloading
class Vector:
  def __init__(self,i,j,k):
    self.i = i
    self.j = j
    self.k = k
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
    
  def __add__(self,v):
    return Vector(self.i + v.i, self.j + v.j, self.k + v.k)
  
v1 = Vector(1,2,3)
print(v1)

v2 = Vector(4,5,6)
print(v2)

print(v1 + v2) # This gives error as we have not defined the __add__ method in the class Vector
print(type(v1 + v2)) # This gives error as we have not defined the __add__ method in the class Vector