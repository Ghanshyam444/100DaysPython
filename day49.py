f = open('day49_1.txt', 'r') # f = open('day49_1.txt')
print(f)
text = f.read()
print(text)
f.close()

fl = open('day49_1.txt', 'a') # this will append the text to the file
fl.write("\nThis is a new line")
fl.close()

fll = open('day49_1.txt', 'w') # this will overwrite the text in the file
fll.write("This is a new line")
fll.close()

flt = open('day49_1.txt', 'rb') # this will read the file in binary mode
print(flt.read())
flt.close()\


# to avoid usage of close() method, we can use the with statement
with open('day49_1.txt', 'r') as f:
  text = f.read()
  print(text)