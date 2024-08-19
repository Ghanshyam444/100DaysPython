# Dictionary Methods

ep1 = {
  122: 45,
  123: 67,
  124: 89,
  125: 90,
}

ep2 = {
  126: 45,
  127: 67,
  128: 89,
  129: 90,
}

ep1.update(ep2) # inserts all the items from one dictionary into another dictionary
print(ep1)
ep2.clear() # removes all the items from the dictionary
print(ep2)
ep1.pop(122) # removes the item with the specified key
print(ep1)
ep1.popitem() # removes the last item from the dictionary
print(ep1)
del ep2 # deletes the dictionary completely

del ep1[123] # removes the item with the specified key
print(ep1)

ep1[123] = 67 # adds an item to the dictionary with the specified key

