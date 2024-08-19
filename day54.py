# is v/s "=="

a = [1,2,43]
b = [1,2,43]

print(a == b) # value 
print(a is b) # exact location of object in memory

# python stores constant values in memory and assigns the same memory location to the variables that have the same value
# this is called interning
# this is why a is b is True
 
# python stores list values in different memory locations
# this is why a == b is True and a is b is False

a = (1,2,43)
b = (1,2,43)
print(a == b) # value
print(a is b) # exact location of object in memory

a = None
b = None
print(a == b) # value
print(a is b) # exact location of object in memory
print(a == None) # value