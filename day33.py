# Python Dictionary
# Dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

dic = {
  "name": "Carla",
  "age": 19,
  "city": "New York"
}
print(dic["name"])
# python 3.7 onwards, the order of the dictionary is preserved earlier it was not preserved i.e it was unordered

print(dic.get("age")) # get method is used to get the value of the specified key

# difference between get and [] is that get will return None if the key is not present in the dictionary but [] will raise an error

print(dic.keys()) # returns a list of all the keys in the dictionary

for keys in dic.keys() : 
  print(keys)
  
print(dic.items()) # returns a list of tuples containing the key value pairs

for key,Value in dic.items() : 
  print(key,Value,sep=" : ")