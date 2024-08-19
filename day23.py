# List Methods
l = [1,2,6,4]
print(l)
l.append(7)

l.sort()
print(l)
l.sort(reverse = True)  
print(l)
l.reverse()
print(l)

print(l.index(6))
print(l.count(6))

m = l # This will create a reference to the list l
m[0] = 0
print(l)

m = l.copy() # This will create a copy of the list l
m[0] = 1
print(l)
print(m)

l.insert(2, 3)
print(l)

m = [900,1000,1100]
l.extend(m)
print(l)
k = l + m
print(k)