import requests

my_headers = {'token': 'oGHZCywaGEkGFoxOLVFOqgZdhgcHHVkE'}
response = requests.get('', headers = my_headers)
print(response.json())

