# assign a variable to open the file in read mode
dollar_spam = open('dollar_menu.txt', 'r')
"""
# use variable.read() to read the file
print(dollar_spam.read())
"""

# to convert items in file into a list for further use
# create an empty list
dollar_menu = []
# loop through the lines in the file and append to the list
for line in dollar_spam:
    # use string method .strip() to remove whitespace, which includes newline characters,
    # otherwise it will print like so: ['cheeky spam\n', 'cheerio spam\n', 'pip pip spam']
    line = line.strip() #updates line variable with stripped version
    dollar_menu.append(line)
print(dollar_menu)

# close the file at the end
dollar_spam.close()