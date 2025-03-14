import requests
from config import NEWSAPI_KEY

def News(query):
    url = (f'https://newsapi.org/v2/everything?'
           f'q={query}&'
           f'sortBy=popularity&'
           f'apiKey={NEWSAPI_KEY}')
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error:", response.json().get("message", "Failed to fetch news."))
        return []
    
    data = response.json()
    articles = data.get("articles", [])

    if not articles:
        print("No articles found for the given query.")
        return []

    ar = [f"Number {i+1}: {article['title']}" for i, article in enumerate(articles[:3])]
    
    return ar
