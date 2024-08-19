# Walrus Operator
# The walrus operator is a new feature in Python 3.8 that allows you to assign values to variables as part of an expression.

a = True
print(a:=False)

numbers = [1,2,3,4,5,6,7,8,9,10]

while (n:= len(numbers)) > 0:
  print(numbers.pop())
  
# Walrus Operator #

#foods = list()
#while True:
 # food = input("What food do you like? ")
  #if food == "quit":
   # break
  #foods.append(food)
  
foods = list()
while(food := input("What food do you like? ")) != "quit":
  foods.append(food)