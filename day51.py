# Seek and Tell
# Seek and Tell are two methods that are used to move the cursor in a file.
with open('day51_1.txt', 'r') as f:
  print(type(f))
# Move to 10th byte in file
  f.seek(10)

# read next 5 bytes
  print(f.tell()) # this will print the current position of the cursor
  data = f.read(5)
  print(data)
  
with open('day51_2.txt', 'w') as f:
  f.write("Hello World")
  f.truncate(5) # this will truncate the file to 5 bytes
  
with open('day51_2.txt', 'r') as f:
  print(f.read()) # this will print the contents of the file