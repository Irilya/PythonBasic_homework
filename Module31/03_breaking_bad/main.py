import requests
import json


result_req = requests.get('https://breakingbadapi.com/api/deaths')

death_data = json.loads(result_req.text)

max_death_data = max(death_data, key=lambda elem: elem['number_of_deaths'])

with open('breaking_bad_death.json', 'w') as file:
    json.dump(max_death_data, file, indent=4)
with open('breaking_bad_death.json', 'r') as file:
    print(file.read())
