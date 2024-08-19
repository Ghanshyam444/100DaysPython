f = open('day50_1.txt', 'r') # f = open('day49_1.txt')
i = 0
while True:
  i += 1
  line = f.readline()
  if not line : 
    print(line,type(line))
    break
  m1 = line.split(",")[0]
  m2 = line.split(",")[1]
  m3 = line.split(",")[2]
  print(f"Marks of student {i} are: {m1}, {m2}, {m3}")
f.close()

f = open('day50_1.txt', 'a') # f = open('day49_1.txt')
lines = ['\nline1\n','line2\n','line3\n']
f.writelines(lines) # this will append the text to the file line by line 
# iteratable objects can be passed to writelines() method
# write() method can be used to write a single string

f.close()