import streamlit as st
import requests

API_key='hNSAh7ClO9Wt9bU12pyIIygFZJrsbA5iKKa1FSbZ'

url='https://api.nasa.gov/planetary/apod?api_key=hNSAh7ClO9Wt9bU12pyIIygFZJrsbA5iKKa1FSbZ'

request = requests.get(url)

content = request.json()

header = content['title']
description = content['explanation']
img_url = content['url']
copyright = content['copyright']

img_response = requests.get(img_url)
img_content = img_response.content
with open('image.jpg', 'wb') as file:
    file.write(img_content)

st.set_page_config(layout='wide')

st.title("NASA's Astronomy Picture of the Day")
st.header(header)
st.image('image.jpg')
st.write(description)
st.header(f'Copyright: {copyright}')
