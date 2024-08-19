# Generators in Python
# Generators are a special class of functions that simplify the task of writing iterators.

def my_generator():
  for i in range(10):
    yield i
    
gen = my_generator()
print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

for i in gen:
  print(i)
