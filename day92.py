# Function Caching
# Function caching is a technique of storing the results of expensive function calls and returning the cached result when the same inputs occur again.

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
  time.sleep(5)
  return n*5

print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")

# The output of the above function is memoized for those values
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6") 

