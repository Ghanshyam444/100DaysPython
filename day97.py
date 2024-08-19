# Multithreading in Python
# Multithreading is a way to introduce concurrency in a program.
# It is a way to run multiple tasks simultaneously.
# Multithreading can be achieved by using the threading module in Python.

import threading
import time
from concurrent.futures import ThreadPoolExecutor
# Indicates some task being done
def func(seconds):
  print(f"Sleeping for {seconds} second(s)")
  time.sleep(seconds)
  return seconds
  
time1 = time.perf_counter()
# normal code
#func(4)
#func(2)
#func(1)
# time2 = time.perf_counter()
#print(time2 - time1)
# Same code using threads
t1 = threading.Thread(target=func, args=[4]) # create a thread
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start() # start the thread
t2.start()
t3.start()

t1.join() # wait for the thread to finish
t2.join()
t3.join()

time2 = time.perf_counter() # get the time after the threads have finished
print(time2 - time1)

def poolingDemo():
  with ThreadPoolExecutor() as executor:
    #future1 = executor.submit(func,3)
    #future2 = executor.submit(func,2)
    #future3 = executor.submit(func,4)
    #print(future1.result())
    #print(future2.result())
    #print(future3.result())
    l = [3,5,1,2]
    results = executor.map(func, l)
    for result in results:
      print(result)
    
poolingDemo()