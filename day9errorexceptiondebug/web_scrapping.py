import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
url = 'https://example.com'

# Fetch the content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)
# Suppose we're scraping article titles and links from a blog
articles = soup.find_all('p')
data = []
print(articles)

for article in articles:
    # print(article.text)
    # title = article.find('p').text
    # link = article.find('p')['href']
    
    data.append({
        'title': article.text,
        # 'link': link
    })

# Save the extracted data as JSON
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data saved to data.json")
