# for and while loops

name = "Abhishek"
for i in name:
  print(i)
  if(i == "b"):
    print("this is something special!")
    
colors = ["red", "blue", "green", "yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)
    
for k in range(0, 101, 3): # 51 to 100 as range is exclusive of the last number 
  print(k+1)