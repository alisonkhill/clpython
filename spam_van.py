# ACCESSING DATA AS JSON
# how data will look in a json file
first_item = {
    'name': 'Spam n Eggs',
    'description': 'Two eggs with Spam',
    'price':2.50}

second_item = {
    'name': 'Spam n Jam',
    'description': 'Biscuit with Jam with Spam',
    'price':3.50}

# How to access and use data in the json format:
# Creating a list of menu items
menu_items = [first_item, second_item]

# Call items in menu_items list by their index
# Each menu item is a dictionary, so you call those by their keys
print(menu_items[0]['name'], menu_items[0]['price'], menu_items[0]['description'])
print(menu_items[1]['name'], menu_items[1]['price'], menu_items[1]['description'])


# EXAMPLE USING URL INSTEAD OF HARD-CODING ITEMS
import requests

my_request = requests.get('http://go.codeschool.com/spamvanmenu')

menu_list = my_request.json()

print("Today's Menu:")
for item in menu_list:
    print(item['name'], ': ', item['desc'].title(), ', $', item['price'], sep='')