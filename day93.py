# News API 

import requests 
import json
query = input("What type of news do you want to read about? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-07-19&sortBy=publishedAt&apiKey=667040295e9c4fb3b143fe0ece8b14d0"
r = requests.get(url)
news = json.loads(r.text)
# print(news,type(news))
for article in news['articles']:
  print(article['title'])
  #print(article['description'])
  print("------------------------------------------------")