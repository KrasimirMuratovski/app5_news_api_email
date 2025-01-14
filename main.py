import send_email
import requests as re

from datetime import datetime

today = datetime.now()
today = today.strftime("%y-%m-%d")

api_key="187643a5a4e34174ab357a24f96fbd1b"
topic = 'Trump'
url = (f"https://newsapi.org/v2/everything?q={topic}&from={today}&sortBy="
	   "publishedAt&apiKey=187643a5a4e34174ab357a24f96fbd1b&language=en")

request = re.get(url)
# content = request.text# THIS WILL PRODUCE str FORMAT
content = request.json()#

to_send = "Subject: Today's news" +'\n'
for article in content["articles"][:5]:
	if article["title"] is not None:
		to_send = (to_send + str(article["title"])+'\n'
				   + article["description"]+ '\n'
				   + article["url"]+2*'\n')

to_send = to_send.encode('utf-8')
send_email.send_email(to_send)