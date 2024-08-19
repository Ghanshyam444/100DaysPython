# Manipulating Tuples
#  Tuples are immutable but you can create new tuples from existing tuples

countries = ("India", "USA", "UK", "Canada")
temp = list(countries) # convert tuple to list
temp.append("Australia") # add new element
temp.pop(3) # remove element at index 3
temp[2] = "Finland" # change element at index 2
countries = tuple(temp) # convert list to tuple
print(countries)

tuple1 = (1,2,3,4,5)
tuple2 = (6,7,8,9,10)
tuple = tuple1 + tuple2
print(tuple) 

print(len(tuple))
print(tuple.count(3))
print(tuple.index(3))
res = tuple.index(3,4,8)
print(res) # find 3 between index 4 and 8