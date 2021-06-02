from selenium import webdriver #Selenium can be used for testing with chrome. 
from bs4 import BeautifulSoup # Need to import from bs4 not BeautifulSoup bc that 'bs4' is the new version
import pandas as pd

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver = webdriver.Chrome() # can specify chrome's location but not necessary.
driver.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2') # as per tutorial

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser') #'html parse' tells us which parser to use (recommended?)
 # Using fina and find all to gather all the data from the html containers. 
for a in soup.findAll('a', href=True, attrs={'class':'_1fQZEK'}): #href=True, 
    name=a.find('div', attrs={'class':'_4rR01T'}) # attrs is attributes?
    # print(name.text)
    price=a.find('div', attrs={'class' :'_30jeq3 _1_WHN1'}) # div is the command like h1 or a etc...
    # print(price.text)
    products.append(name.text)
    prices.append(price.text)
# print(products)
# print(prices)
df = pd.DataFrame({'Product Name':products,'Price':prices}) #Puts this into an excel file
df.to_csv('products.csv', index=False, encoding='utf-8')

