#list

marks = [3,5,6,"Harry",True,6,7,2,32,345]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

print(marks[-3]) # it works same as print(marks[len(marks)-3])

if 3 in marks:
  print("3 is present in the list")
else:
  print("3 is not present in the list")

# same things apply to strings as well
if "arry" in "harry":
  print("arry is present in harry")
  
print(marks)
print(marks[1:-1])
print(marks[1:4:2]) # jump index by 2

# List Comprehension

lst = [i*i for i in range(10) if i%2 == 0]
print(lst)
