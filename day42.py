# Enumerate function in Python
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

'''
marks = [12,56,78,34,90,1,4]
index = 0
for mark in marks:
  print(mark)
  if(index == 3):
    print("The loop is terminated")
  index += 1
'''

# The above code can be written using enumerate function as below

marks = [12,56,78,34,90,1,4]
for index,mark in enumerate(marks):
  print(mark)
  if(index == 3):
    print("The loop is terminated")
    
# Enumerate function can start from any index as below

for index,mark in enumerate(marks, start = 1):
  print(index,mark)
  