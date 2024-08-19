# String Methods
# Strings are immutable in python i.e. once a string is created, it cannot be changed.
# 
a = "!!!harry !!!!! harry"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.lstrip("!"))
print(a.replace("!", "@"))
print(a.split(" "))
titlee = "Introduction to Python"
print(titlee.capitalize())
str1 = "Welcome to Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(str1.center(50))
print(a.count("harry"))

print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))

str2 = "He is name is Dan. he is an honest man"
print(str2.find("is"))
print(str2.find("is", 5))
print(str2.find("100"))
#print(str2.index("100")) # it will throw an error
print(str2.index("is"))

str3 = "WecomeToTheConsole\n"
print(str3.isalnum()) # it is alphanumeric
print(str3.isalpha()) # it is alphabetic
print(str3.islower()) # it is digit
print(str3.isprintable) # this method returns true if all the characters are printable

print(str3.isspace()) # It returns true if all the characters are whitespaces
str4 = "World Health Organization"
print(str4.istitle()) # It returns true if the string is in title case

print(str1.startswith("Welcome"))

print(str4.swapcase()) # It swaps the case of the string

print(str2.title())