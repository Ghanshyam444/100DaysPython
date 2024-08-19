# Custom Errors in Python
# You can create your own errors in Python. Below is an example of how to create a custom error class:

a = int(input("Enter a number between 5 and 9 : "))

if(a<5 or a>9):
  raise Exception("Number is not in the range of 5 to 9")
if(a==5):
  raise ValueError("Number is 5")