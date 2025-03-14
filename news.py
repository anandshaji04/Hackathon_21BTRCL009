import requests
from config import *

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2025-03-14&'
       'sortBy=popularity&'
       'apiKey=NEWSAPI_KEY')

response = requests.get(url)
