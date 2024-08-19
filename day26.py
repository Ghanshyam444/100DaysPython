import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)

if(hour > 0 and hour < 12):
  print("Good Morning!")
elif(hour >= 12 and hour < 16):
  print("Good Afternoon!")
if(hour >= 16 or hour < 0):
  print("Good Night Sir!")