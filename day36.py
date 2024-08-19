# Error Handling in Python
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

a = input("Enter a number : ")
print(f"Multiplication table of {a} is : ")

try: 
  for i in range(1, 11):
    print(f"{int(a)} * {i} = {a*i}")
except Exception as e:
  print(e)
  print("Please enter a valid number")

print("Some line of code")
print("End of the program")


try:
  num = int(input("Enter a number : "))
  a = [6,3]
  print(a[num])
except ValueError:
  print("Please enter a valid number")
except IndexError:
  print("Index out of range")