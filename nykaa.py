import requests
from bs4 import BeautifulSoup as bs
from requests import Session
s=Session()
import pandas as pd
all_pro=[]
img_p=[]
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
url='https://www.nykaa.com/mom-baby/maternity-care/breast-firming-gels-creams/c/14839'
r=s.get(url)
soup=bs(r.text,'html.parser')
pro=soup.find_all('div','css-jtn0l5')
for i in pro:
    name=i.find('div','css-xrzmfa').text
    if i.find('span','css-17x46n5'):
      original_price=i.find('span','css-17x46n5').text
    else:
        ''  
    d_price=i.find('span','css-111z9ua').text    
    u_url=i.find('a').get('href')
    p_url='https://www.nykaa.com'+u_url
    
    
    r_1=s.get(p_url)
    soup_1=bs(r_1.text,'html.parser')
    item=soup_1.find('div','css-1rruyoa')
    for j in item:
        img=j.find_all('img')
        for z in img:
            
          url_2=z.get('src')
          img_p.append(url_2)
          d={'name':name,'orignal price':original_price,'discounted price':d_price,'product_url':p_url,'imgs':img_p}
          print(d)