# Lambda Functions 
# Lambda functions are small anonymous functions that can have any number of arguments, but can have only one expression.

#def double(x):
#  return x * 2
def appl(fx,value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x ** 3
sum = lambda x,y,z: x + y + z
avg = lambda x, y: (x + y) / 2
print(avg(5, 10))
print(cube(5))
print(double(5))
print(sum(5, 10, 15))
print(appl(cube, 2))
print(lambda x: x ** 3,2)