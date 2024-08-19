# Local v/s Global variables
# Local variables are the variables that are declared inside a function and can be accessed only inside that function.
# Global variables are the variables that are declared outside a function and can be accessed throughout the program.
# Global variables can be accessed inside a function by using the keyword global.


x = 10 # global variable
print(x)

def hello():
  # x = 5 # local variable
  global x
  x = 5
  print(f"The local x is {x}")
  print("Hello Harry")

print(f"The global x is {x}")
hello()
print(f"The global x is {x}")
