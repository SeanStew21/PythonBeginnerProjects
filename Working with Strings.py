#Strings Examples

# \n command makes a new line in a string
#concatenation is appending a string to another string

a_string = "Anything within these quotes"

strings = "Plain text within\nquotation marks"

print(strings + "is what a string is.") #concatenation

#functions in strings
print(a_string.lower()) #.lower() is a function
print(a_string.isupper()) #a boolean function
#the parentheses after function if you enter a value in those parentheses is a parameter. Example:
print(a_string.index("w"))