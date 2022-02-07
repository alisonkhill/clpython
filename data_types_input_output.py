# Single line comments use the hash character
""" 
Multi-line comments use triple quotes,
but it's better to just put a hash in front of each line.
"""
# Checking version of python in Windows: py --version
# Exiting the interpreter = Ctrl+Z

"""
Data types:
int = integer
float - decimal number
string = text
"""

"""
Function syntax:
functionName(argument)

Built in functions:
int() converts to integer
float() converts to decimal
print() returns the value

string concatenating: newString = string1 + " " + string2

input() prompts user for input - always returns a string

strings can be created with single or double quotes depending on if either is used in the string
"""
# Most mathematical operators are the same, but there are some special ones
# // is for integer division - gives you the integer without the remainder
# % (called modulus) gives you the remainder

# \n means new line

# test early and often

age = int(input("How old are you?\n"))
decades = age // 10
years = age % 10
print("You are " + str(decades) + " decades and " + str(years) + " years old.")