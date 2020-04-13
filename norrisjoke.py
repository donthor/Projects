import requests

url = 'https://api.chucknorris.io/jokes/random'
joke = requests.get(url).json()
joke = joke['value']
print(joke)