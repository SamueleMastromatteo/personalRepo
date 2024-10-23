import requests

r = requests.get('https://reqres.in/api/users/2', "id")

print(r.text)