# Short hand if else
a = 330
b = 3303
print("A") if a > b else print("B") if a < b else print("=")
# The above code is equivalent to:
# if a > b: print("A") 
# elif a < b: print("B")
# else: print("=")

c = 9 if a>b else 0 
print(c)