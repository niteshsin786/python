import pprint
import requests

request = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')
#print(request.json()['items'])
#pprint.pprint(request.json()['items'])
for item in request.json()['items']:
    if item['answer_count'] == 0:
        print(item['title'])
        print(item['link'])
    else:
        print('skipped')
