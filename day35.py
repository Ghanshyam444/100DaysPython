# Else with for loop
# Else block will execute only if the loop is not terminated by a break statement.

for i in range(1, 4):
  print(i)
  
else:
  print("The loop is completed")
  
for i in range(1, 4):
  print(i)
  if i == 2:
    break
else:
  print("The loop is completed")
  
# else indicates that the loop is completed normally without any break statement. If the loop is terminated by a break statement then the else block will not be executed.
# also else is used with while loop