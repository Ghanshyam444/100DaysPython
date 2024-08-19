# Finally clause in Python
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
  l = [1,2,3]
  i = int(input("Enter the index : "))
  print(l[i])
except:
  print("An error occured")
  
finally:
  print("Finally block is executed")
  
# Now we can wonder why not to directly write the code after except block, as both will always run, example to demonstrate this is below

def func():
  try:
    l = [1,2,3]
    i = int(input("Enter the index : "))
    print(l[i])
    return 1
  except:
    print("An error occured")
    return 0
  finally:
    print("Finally block is executed")
    
x = func()
print(x)

# so here finally gets executed even if the function returns in try or except block and also if the function returns in finally block
# so finally block is always executed
