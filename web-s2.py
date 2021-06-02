from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver = webdriver.Chrome()
driver.get('https://www.flipkart.com/home-kitchen/kitchen-appliances')

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for a in soup.findAll('div', attrs={'class':'_4ddWXP'}): #href=True, 
    name=a.find('a', attrs={'class':'s1Q9rs'})
    print(name.text)
    price=a.find('div', attrs={'class' :'_30jeq3'})
    print(price.text)
##    rating=a.find('div', attrs={'class':'_3LWZ1K'})
##    print(rating)
    products.append(name.text)
    prices.append(price.text)
##    ratings.append(rating.text)
print(products)
print(prices)
print(ratings)
df = pd.DataFrame({'Product Name':products,'Price':prices}) #,'Rating':ratings
df.to_csv('products2.csv', index=False, encoding='utf-8')
