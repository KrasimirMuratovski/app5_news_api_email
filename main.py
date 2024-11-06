import requests as re

api_key="187643a5a4e34174ab357a24f96fbd1b"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-10-06&sortBy="
	   "publishedAt&apiKey=187643a5a4e34174ab357a24f96fbd1b")

request = re.get(url)
# content = request.text# THIS WILL PRODUCE str FORMAT
content = request.json()#

for article in content["articles"]:
	print(article["title"])