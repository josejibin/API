import requests
import oauth2
import time
import json


url1 ="https://api.twitter.com/1.1/search/tweets.json" 
url2="https://api.twitter.com/1.1/statuses/mentions_timeline.json"
url3="https://api.twitter.com/1.1/followers/list.json"
url4="https://api.twitter.com/1.1/statuses/user_timeline.json" 
url5="https://api.twitter.com/1.1/followers/ids.json"
params = {
"oauth_version": "1.0",
"oauth_nonce": oauth2.generate_nonce(),
"oauth_timestamp": int(time.time())
}

consumer = oauth2.Consumer(key="xxx", secret="xxx")
token = oauth2.Token(key="xxx", secret="xxx")
params["oauth_consumer_key"] = consumer.key
params["oauth_token"] = token.key


#here I use url4 means to get my teets..u can use url1 and give parameters for serach,count,since etc

for i in range(1):
	url = url4
	#params["q"] = "haskell"
	params["count"] = 5
	#params["since_id"] = ""
	#params["max_id"] = ""

	req = oauth2.Request(method="GET", url=url, parameters=params)
	signature_method = oauth2.SignatureMethod_HMAC_SHA1()
	req.sign_request(signature_method, consumer, token)
	headers = req.to_header()
	url = req.to_url()
	print url
	data=(requests.get(url)).json()
	print data
	# data is not formatted
	#print len( data["statuses"])
	

#status_texts = [ status['text'] 
 #               for status in data["statuses"] ]

#print status_texts

 


