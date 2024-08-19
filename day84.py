# TIme Modeule
# The time module provides various time-related functions. For this example, we will use the time.time() function, which returns the current system time in ticks since 12:00am, January 1, 1970(epoch).

import time 


def usingWhile():
  i = 0
  while i< 5000:
    i += 1
    print(i)

def usingFor():
  for i in range(5000):
    print(i)
    
init = time.time()
#usingFor()
t1 = (time.time() - init)
init = time.time()
#usingWhile()
t2 = (time.time() - init)

print(f"Time taken by for loop: {t1}")
print(f"Time taken by while loop: {t2}")


print(4)
time.sleep(3)
print("This is printed after 3 seconds")

t = time.localtime()
formatted = time.strftime("%Y-%M-%D, %H:%M:%S",t)

print(formatted)