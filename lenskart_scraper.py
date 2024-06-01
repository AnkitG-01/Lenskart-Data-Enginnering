import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://www.lenskart.com/eyeglasses.html?pageCount=10"
headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0', 'Accept-Language': 'en-US, en;q=0.5'})
response = requests.get(url, headers=headers)

Title = []
Details = []
Price = []
Ratings = []


soup = BeautifulSoup(response.text, 'html.parser')

for d in soup.find_all('div', attrs={'class':'ProductDetailsContainer--1hartic eQRFAk'}):
    name = d.find('p', attrs={'class':'ProductTitle--xakon1 dZrMkC'}).text
    Title.append(name)

    details = d.find('div', attrs={'class':'ProductSizeContainer--1a4akcf QRMAB'}).text
    Details.append(details)

    price = d.find('span', attrs={'class':'SpecialPriceSpan--1mh26ry gDbhuM'}).text
    Price.append(price)

    ratings = d.find('span', attrs={'class':'NumberedRatingSpan--kts3v6 fXcXid'}).text
    Ratings.append(ratings)

if len(Ratings)!=len(Price):
    Ratings+=[0]*(len(Price)-len(Ratings))

df = pd.DataFrame({'Product Name': Title, 'Details': Details, 'Price': Price, 'Rating': Ratings})
print(df)
df.to_csv('C:/Users/Ankit1/Desktop/Projects/Web Scraping/Lenskart_Data.csv')
    
