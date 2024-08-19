# Decorators in Python
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.

def greet(func):
  def mfx(*args,**kwargs):
    print("Greetings from the decorator")
    func(*args,**kwargs)
    print("Thanks for using this function")
  return mfx
  
@greet
def hello():
  print("Hello Harry")

@greet
def add(a,b):
  print(a+b)

hello()
greet(add)(2,3)