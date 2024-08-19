for i in range(12):
  if(i == 10):
    continue # This will skip the current iteration and continue with the next iteration
  print("5 X ", i, " = ", 5*i)
    # break # This will break the loop and come out of the loop

print("End of the program")


# Emulate the do while loop in python
i = 0 
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break