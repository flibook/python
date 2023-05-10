import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
dict = response.json()
max_intelligence = 0

for k in dict:
    if k['powerstats']['intelligence'] > max_intelligence and k['name'] in ['Hulk', 'Captain America', 'Thanos']:
        max_intelligence = k['powerstats']['intelligence']
        res = k

print(f'Супер интеллектуальный герой: {res["name"]} {res["powerstats"]["intelligence"]}')
