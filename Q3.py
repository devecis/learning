"""
Hard (It's not that hard):

Join us Wednesday at 2 PM for this problem!
Find a REST API that interests you. List here:  https://github.com/public-apis/public-apis
Download a JSON from that api, using the requests (or requests-html) library in Python
Convert that JSON to a dictionary, using the JSON library.
Using the .keys() function, explore your dictionary some. What keys are available? How far down the tree do you have to go to find the data you wanted?
What else is available in your JSON? Is there a next link? Other metadata?

Likely not covered Wednesday:
Google sheets (Think excel, on google's platform) has an excellent API that allows you to GET and POST data to and from a sheet.
Read about it here: https://developers.google.com/sheets/api/reference/rest
Can you build an API call to push your data from above to a sheet? It's pretty easy!
Think about the power here- Could you schedule a script like the first half to pull data on a schedule, and post to sheets? Pretty convenient!

"""

import requests
import json

URL = 'https://rickandmortyapi.com/api/character'

r = requests.get(URL)
characters = json.loads(r.content)
results = characters['results']
print("Who are the characters from Rick and Morty")
for item in results:
    print(item['name'], item['status'], item['species'], item['gender'])
    print("Wubba lubba dub dub\n" * 10)