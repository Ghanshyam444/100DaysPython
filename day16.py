# Match case Statements
x = int(input("Enter a number: "))
# x is a variable to match
# not necessary to use break in python
match x:
  case 0:
    print("x is 0")
    # case with if-condition
  case 4: 
    print("x is 4")
  
  case _ if x!=90:
    print("x is not 90")
  case _ if x!=80:
    print("x is not 80")
  case _:
    print(x)
    