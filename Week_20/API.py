import json
import requests

insults = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
a = insults.json()
b = json.dumps(a, indent=2)
c = 
print (b)

