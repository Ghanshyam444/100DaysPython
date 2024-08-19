# Doc Strings
# Doc Strings are used to describe the purpose of a function, class or module.
# It is written in triple quotes.

def square(x): # Doc string should be written below the function definition
  """This function returns the square of a number"""
  return x*x

print(square(5))
print(square.__doc__) # This will print the doc string of the function

# PEP 8 - Python Enhancement Proposal
# It is a style guide for python code.
# It is used to write readable code.
# It is recommended to follow the PEP 8 style guide.
# In terminal write python
# in that python script write import this

# Some of the rules are:
# 1. Use 4 spaces for indentation
# 2. Limit all lines to a maximum of 79 characters
# 3. Use blank lines to separate functions and classes and larger blocks of code inside functions
# 4. Use spaces around operators and after commas
# 5. Use docstrings
# 6. Use spaces around arithmetic operators
# 7. Avoid extraneous whitespace
# 8. Use lowercase with underscores for variable names
# 9. Use a space after a comma
# 10. Use a space after a colon
# 11. Use spaces around assignment operators
# 12. Use spaces around the parameter list
# 13. Use spaces around the default value of a parameter
# 14. Use spaces around the keyword arguments
# 15. Use spaces around the keyword arguments in a function call
# 16. Use spaces around the keyword arguments in a function definition