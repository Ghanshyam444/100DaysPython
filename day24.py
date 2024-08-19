# Tuples in Python
# Tuples are similar to lists but they are immutable i.e. they cannot be changed.

tup1 = (1,5,6,342,32,"green",True)
print(type(tup1),tup1)

tup2 = (1,)
print(type(tup2),tup2)
# It does not allow tup2[0] = 5

# use tupe to get features of constant list
print(tup1[1])
print(tup1[1:4])
print(tup1[1:-1])

if 342 in tup1:
  print("342 is present in the tuple")
  
tup2 = tup1[1:4]
print(tup2)