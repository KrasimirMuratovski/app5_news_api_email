import send_email
import requests as re

api_key="187643a5a4e34174ab357a24f96fbd1b"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-10-06&sortBy="
	   "publishedAt&apiKey=187643a5a4e34174ab357a24f96fbd1b")

request = re.get(url)
# content = request.text# THIS WILL PRODUCE str FORMAT
content = request.json()#

to_send = ''
for article in content["articles"]:
	if article["title"] is not None:
		to_send+=str(article["title"])+'\n' + article["description"]+2*'\n'

to_send = to_send.encode('utf-8')
send_email.send_email(to_send)