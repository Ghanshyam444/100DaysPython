# Hybrid Inheritance and Hierarchical Inheritance
# Hybrid inheritance is a combination of multiple and multilevel inheritance.
# Hierarchical inheritance involves multiple derived classes inheriting from a single base class.

# Hybrid Inheritance
class BaseClass:
  pass 

class Derived1(BaseClass):
  pass

class Derived2(BaseClass):
  pass 

class Derived3(Derived1,Derived2):
  pass

# Hierarchial Inheritance

class BaseClass:
  pass

class Derived1(BaseClass):
  pass

class Derived2(BaseClass):
  pass

class Derived3(Derived1):
  pass


