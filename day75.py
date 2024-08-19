# Visit png egg website to download some png images to test the program.
import os 
files = os.listdir("day75")
i = 1
for file in files:
  if file.endswith(".png"):
   print(file)
   os.rename(f"day75/{file}", f"day75/{i}.png")
   i += 1
# os.rename("day75/file1.txt","day75/file.txt")