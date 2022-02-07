# keys mapped to values

# syntax:
dictionary = {'key': 'value'}

# create empty dictionary
dictionary = {} 
    
# To add and to update:
dictionary[key] = value
print(dictionary) # prints {key: value}

# To delete:
del dictionary[key]

acronyms = {
    'LOL': 'laughing out loud',
    'IDK': "I don't know",
    'TBH': 'To be honest'
}

# instead of using the index number, use the key to call the associated value: 
print(acronyms['LOL']) # laughing out loud will print

# use the get method to access values by their keys
dictionary.get(key)

# Trying to access a key that doesn't exist causes a KeyError
    # You can avoid this using the get method. So if you're not sure whether a key is present:
        definition = dictionary.get(key)
        print(defintion) 
        # Prints "none" if key doesn't exist
        
    # To make it understandable to the user, you can use an if statement to provide a message instead of just 'none'
        if definition: # simply means if definition exists
            print(definition)
        else:
            print("Key doesn't exist.")
    # none evaluates to false in a conditional statement
