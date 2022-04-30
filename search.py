import requests
import random
from bs4 import BeautifulSoup
from lxml import html

    
ety = input("request ")
e = []
url = 'https://yandex.ru/images/search?from=tabbar&text='+ety
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
images = soup.find_all('img')
    
for image in images:
        
    src = image.get("src")    
        
    if src:
        e.append(src)
tr = random.randint(0,len(e)-1)

print('https:'+str(e[tr]))#tehnologii 
   
   
