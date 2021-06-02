from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver = webdriver.Chrome()
driver.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2')

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for a in soup.findAll('a', href=True, attrs={'class':'_1fQZEK'}): #href=True, 
    name=a.find('div', attrs={'class':'_4rR01T'})
    print(name.text)
    price=a.find('div', attrs={'class' :'_30jeq3 _1_WHN1'})
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
df.to_csv('products.csv', index=False, encoding='utf-8')
#C:\Users\AnikaP\AppData\Local\Programs\Python\Python39
##import time
##from selenium import webdriver
##
##driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
##driver.get('http://www.google.com/');
##time.sleep(5) # Let the user actually see something!
##search_box = driver.find_element_by_name('q')
##search_box.send_keys('ChromeDriver')
##search_box.submit()
##time.sleep(5) # Let the user actually see something!
##driver.quit()
