# map, filter and reduce
def cube(x):
  return x ** 3

print(cube(2))

l = [1, 2, 3, 4, 5, 6]
#newl  = []
#for item in l:
#  newl.append(cube(item))
  
#print(newl)

# newl = list(map(cube, l)) # map applies the function to all the elements of the list
newl = list(map(lambda x: x ** 3, l))
print(newl)

def filter_function(a):
  return a>4

newnewl = list(filter(lambda x: x>4, l)) # filter filters the elements of the list based on the function
print(newnewl)

# reduce is not a built-in function in python 3
from functools import reduce
sum = reduce(lambda x, y: x + y, l) # reduce applies the function cumulatively to the elements of the list
print(sum)