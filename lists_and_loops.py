# lists are like arrays in javascript. 
# they are zero indexed, so if you want the item at index n, you should call n-1

empty_list = []


# list.method()

acronyms = ['LOL', 'OMG', 'IDK', 'SMH', 'TBH']

acronyms.append('BFN')
acronyms.remove('LOL')
del acronyms[1]
print(acronyms)


# to check if an item exists in the list
word = 'TBH'

if word in acronyms:
    print(word + ' is in the list')
else:
    print(nope)

# to print each item in a list, use a loop to go through the whole list:

for word in acronyms:
    print(word)



