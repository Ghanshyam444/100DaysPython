# what is if _name_ == "_main_": in python
# The _name_ variable is a special variable in Python that is automatically created when the program is executed.
# The value of the _name_ variable is set to "_main_" when the program is executed as the main program.
# This allows you to determine whether the program is being run as the main program or being imported as a module.

import day45_1 as harry

# even if we import the module, the code inside the module will run
# this problem is solved by using if __name__ == "__main__"

harry.welcome() # this will run the code inside the module



