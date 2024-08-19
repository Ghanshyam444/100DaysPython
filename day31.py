# Set
# set is used to store multiple items in a single variable.
# It is unordered and unindexed.
# It does not allow duplicate values.

s = {2,4,2,6}
print(s)
# It will not allow s[0] = 5 because it is unindexed and unordered set of values 
info = {"Carla",1,False,5.9,19}
print(info)

harry = {10,}
print(type(harry))

hel =  set()
print(type(hel)) 

for value in info : 
  print(value)
  
k = [1,2,3,4,5,6,7,8,9,10]
l = set(k)
print(l)