# what are f-strings ??
# These are formatted string literals. They are prefixed with 'f' or 'F'. They are similar to the format() method of strings.

letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Abhishek"

print(letter.format(name, country))

print(f"Hey my name is {name} and I am from {country}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.211444))

pricee = 49.211444
print(f"For only {pricee:.2f} dollars!")

print(f"{20*30}")

print(f"Hey my name is {{name}} and I am from {{country}}")
