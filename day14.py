# Conditional Statements
a = int(input("Enter your age: "))
# Conditional operators
# >, <, >=, <=, ==, !=
# Logical operators
# and, or, not
if(a>18):
  print("You can drive")
else:
  print("You cannot drive")
  
num = int(input("Enter a number: "))
if(num<0):
  print("Negative number")
elif(num==0):
  print("Zero")
else:
  print("Positive number")
  
# Nested if-else
if(num>0):
  if(num%2==0):
    print("Even number")
  elif(num==0):
    print("Zero")
  else:
    print("Odd number")
else:
  print("Invalid number")