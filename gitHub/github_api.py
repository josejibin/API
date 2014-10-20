
API_TOKEN='xxx'
GIT_API_URL='https://api.github.com'

import requests


url1='https://api.github.com'

url='https://api.github.com/user/repos'

#fields = "id,name,birthday"
fields = "id"
limit=4

url = '%s?access_token=%s' % \
    (url,API_TOKEN,)

r = requests.get(url).json()
#print r
print type(r)
for data in r:
	print data["full_name"]

