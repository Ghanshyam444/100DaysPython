# Set Methods
# union() - returns a new set with all items from both sets
# update() - inserts all the items from one set into another set
# we use update method to insert into the calliing object and union method to return a new set
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2) # s1 = s1.union(s2) 
print(s1,s2)

s3 = s1.intersection(s2)
print(s3)

s1.intersection_update(s2)
print(s1)

a1 = {1,2,5,6}
a2 = {3,6,5,7}
a3 = a1.symmetric_difference(a2) # returns a new set with all items from both sets except the common items
print(a3)
a4 = a1.difference(a2) # returns a new set with all items from the first set except the common items
print(a4) # a1 - a2
a1.difference_update(a2) # removes the common items from the first set
print(a1)

k1 = {1,2,5,6}
k2 = {3,7}

print(k1.isdisjoint(k2)) # returns True if there are no common items in both sets

l1 = {1,2,5,6}
l2 = {1,2}

print(l1.issuperset(l2)) # returns True if all items in the specified set are present in the calling set

print(l2.issubset(l1)) # returns True if all items in the specified set are present in the calling set

l1.add(10) # adds an element to the set
print(l1)
l1.remove(10) # removes the specified element from the set
print(l1)

l1.discard(5) # removes the specified element from the set 

# difference between remove and discard is that remove will raise an error if the element is not present in the set

k = l1.pop() # removes the last element from the set 
print(k) # we can't predict which element will be removed

del l1 # deletes the set l1 completely

l2.clear() # removes all the elements from the set
print(l2)

info = {"Carla",1,False,5.9,19}

if "Carla" in info : 
  print("Yes")
else :
  print("No")
