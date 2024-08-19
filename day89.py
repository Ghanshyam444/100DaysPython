# Request Module
# pip install requests
# requests is a Python module that you can use to send all kinds of HTTP requests.
# It is an easy-to-use library with a lot of features ranging from passing parameters in URLs to sending custom headers and SSL Verification.

import requests

# response = requests.get('https://www.google.com') # get request to google.com website and store the response in response variable
# print(response.text)

url = "https://jsonplaceholder.typicode.com/posts" # url to get the posts

data = {
    "title": "ghanshyam",
    "body": "bhai",
    "userId": 21,
}

headers = {
  'Content-type' : 'application/json; charset=UTF-8'
}
response = requests.post(url,headers=headers, json=data) # post request to the url with the data and headers

print(response.text) # print the response

url2 = "https://www.codewithharry.com/blogpost/django-cheatsheet/"

r = requests.get(url2) # get request to the url2

# bs4 is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'html.parser') # parse the response text using html.parser

print(soup.prettify()) # print the response in a pretty format

for heading in soup.find_all("h2"):
  print(heading.text) # print all the h2 tags
  