import requests as re
import streamlit as st

# api = "W8carBHIz6lbfbLYGbrD5ZKP7MEYbd9xfhzlAcjU"
get_url = "https://api.nasa.gov/planetary/apod?api_key=W8carBHIz6lbfbLYGbrD5ZKP7MEYbd9xfhzlAcjU"
#1st call
response = re.get(get_url)
data = response.json()## transforms response.content to dict

title = data["title"]
explanation = data["explanation"]
image_url=data["url"]

image_response = re.get(image_url)
image_data=image_response.content## direct image binary data

with open("image.jpg", 'wb') as image_file:
	image_file.write(image_data)


st.text(title)
st.image("image.jpg")
st.write(explanation)