# Getters and Setters in Python
# Getters and Setters are used to protect your data from directly being accessed by the user.
# Getters are used to get the value of a private attribute.
# Setters are used to set the value of a private attribute.

class MyClass:
  def __init__(self,value):
    self._value = value
  def show(self):
    print(self._value)
  @property # this is a getter method which is used to get the value of a private attribute
  def ten_value(self):
    return 10 * self._value
  
  @ten_value.setter # this is a setter method which is used to set the value of a private attribute
  def ten_value(self,value):
    self._value = value / 10
  
obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()