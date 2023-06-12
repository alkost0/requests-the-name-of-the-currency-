import requests

response = requests.get('https://api.github.com')

url = 'https://api.github.com/search/repositories'
params = {'q': 'python', 'sort': 'stars'}
response = requests.get(url, params=params)
# Эквивалентно URL с параметрами
url = 'https://api.github.com/search/repositories?q=python&sort=stars'

print(response.status_code)
print(response.content)