# try, except blocks catch errors so we can avoid a program crash
try: # try to do this, move to except if there's an error
    file = open('stales.txt', 'r')
    print(file.read())
except: # instead of stopping the program, you get feedback and can continue the rest of the program
    print('File does not exist')


# there are over 60 types of exceptions in python
# for example, ValueError
price = input('Enter the price\n')

try:
    price = float(price)
    print('Price:', price)
except ValueError:
    print('Nope')


# instead of using a custom error message like Nope, 
# you can print the actual error message from the interpreter
try:
    price = float(price)
    print('Price:', price)
except ValueError as err:
    print(err)