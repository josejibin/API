#take photoes from my fb account gibin






import requests 
import json


ACCESS_TOKEN = 'xxx'
base_url = 'https://graph.facebook.com'
url1='https://graph.facebook.com/me/photos'
fields = 'images'
limit=4
url = '%s?limit=%d&fields=%s&access_token=%s' % \
    (url1, limit, fields, ACCESS_TOKEN,)

content = requests.get(url).json()
sources=[]

for data in content['data']:
	sources.append({ "id":data["id"],"source":data["images"][0]["source"]})


for d in sources:
	print d
print type(content['data'])
print content.keys()

