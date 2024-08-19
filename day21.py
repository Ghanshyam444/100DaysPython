def average(a=4,b=1):
  print("Average of two numbers is ", (a+b)/2)
# starting parameters of the function can be necessary arguments but the last parameters can be optional arguments
average(4,6)
average(b = 9)
average(8)
average(b = 9, a = 10)

def avg(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  return ("Average of the numbers is ", sum/len(numbers))
  
c = avg(1,2,3,4,5,6,7,8,9,10)
print(c)