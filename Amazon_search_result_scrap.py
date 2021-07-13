#%% 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

import os
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import codecs
import csv
import pdb
import random
from fake_useragent import UserAgent

#%%

def add_to_csv(prd_name):
	with codecs.open("Product_page.csv", 'a', 'utf-8') as file:
		writer = csv.writer(file)
		writer.writerow(["",prd_name])


def retrive_proxy():
    proxies_req = Request('https://www.sslproxies.org/')
    proxies_req.add_header('User-Agent', ua.random)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')
    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
        'ip':   row.find_all('td')[0].string,
        'port': row.find_all('td')[1].string
    })

def random_proxy():
      return random.randint(0, len(proxies) - 1)

def get_soup(URL):
    try:
        proxy_index = random_proxy()
        proxy = proxies[proxy_index]
        selected_proxy = proxy['ip'] + ':' + proxy['port']
        page = requests.get(URL, headers, selected_proxy)
        # print(headers, proxies)
        soup = BeautifulSoup(page.content, 'html.parser')
        # soup = BeautifulSoup(re.sub("<!--|-->","", page), "lxml")
        return soup
    except:
        exit(0)
            
    return

def get_soup_no_header(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def navi_pages(URL):
    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    product_list=soup.find('div',class_='s-main-slot s-result-list s-search-results sg-row').find_all('div',class_='a-section a-spacing-none')    
    for index,items in enumerate(product_list):
        # print(items.find_all('div',class_='').)
        if (items.find('span',class_='a-size-base-plus a-color-base a-text-normal')):
            print(index,items.find('span',class_='a-size-base-plus a-color-base a-text-normal').get_text())
            prd_name=items.find('span',class_='a-size-base-plus a-color-base a-text-normal').get_text()
            add_to_csv(prd_name)
    page_check=soup.find('div',class_='a-section a-spacing-none a-padding-base')
        
    if (page_check.find('li',class_='a-disabled a-last')):
        print('end of page') 
    else:
        print('next page')
        page_nav=soup.find('li',class_='a-last').find('a')  
        next_page=('https://www.amazon.in'+page_nav.get('href'))  
        print(next_page)  
        navi_pages(next_page)  



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

print("complete")

#%%

# Input Product page link
URL='https://www.amazon.in/s?k=grocery+items+all&rh=p_n_is_pantry%3A9574335031&dc&crid=LKS3P1D0J02D&qid=1626088204&rnid=9574334031&sprefix=groc%2Caps%2C368&ref=sr_nr_p_n_is_pantry_1'
navi_pages(URL)






#%%


# product_list=soup.find('div',class_='s-main-slot s-result-list s-search-results sg-row').find_all('div',class_='a-section a-spacing-none')

# for index,items in enumerate(product_list):
#     # print(items.find_all('div',class_='').)
#     if (items.find('span',class_='a-size-base-plus a-color-base a-text-normal')):
#         print(index,items.find('span',class_='a-size-base-plus a-color-base a-text-normal').get_text())
    
# page_check=soup.find('div',class_='a-section a-spacing-none a-padding-base')
    
# if (page_check.find('li',class_='a-disabled a-last')):
#     print('end of page') 
# else:
#     print('next page')
#     page_nav=soup.find('li',class_='a-last').find('a')  
#     next_page=('https://www.amazon.in'+page_nav.get('href'))  
#     print(next_page)
#     # navi_pages(next_page)

# # %%
# r = requests.get(next_page, headers=headers)

# # print(r) # print request to see if Response 200

# soup = BeautifulSoup(r.content, "html.parser")
# product_list=soup.find('div',class_='s-main-slot s-result-list s-search-results sg-row').find_all('div',class_='a-section a-spacing-none')

# for index,items in enumerate(product_list):
#     # print(items.find_all('div',class_='').)
#     if (items.find('span',class_='a-size-base-plus a-color-base a-text-normal')):
#         print(index,items.find('span',class_='a-size-base-plus a-color-base a-text-normal').get_text())
    
# page_check=soup.find('div',class_='a-section a-spacing-none a-padding-base')
    
# if (page_check.find('li',class_='a-disabled a-last')):
#     print('end of page') 
# else:
#     print('next page')
#     page_nav=soup.find('li',class_='a-last').find('a')  
#     next_page=('https://www.amazon.in'+page_nav.get('href'))  
#     print(next_page)
# # %%
# r = requests.get(next_page, headers=headers)

# # print(r) # print request to see if Response 200

# soup = BeautifulSoup(r.content, "html.parser")
# product_list=soup.find('div',class_='s-main-slot s-result-list s-search-results sg-row').find_all('div',class_='a-section a-spacing-none')

# for index,items in enumerate(product_list):
#     # print(items.find_all('div',class_='').)
#     if (items.find('span',class_='a-size-base-plus a-color-base a-text-normal')):
#         print(index,items.find('span',class_='a-size-base-plus a-color-base a-text-normal').get_text())
    
# page_check=soup.find('div',class_='a-section a-spacing-none a-padding-base')
    
# if (page_check.find('li',class_='a-disabled a-last')):
#     print('end of page') 
# else:
#     print('next page')
#     page_nav=soup.find('li',class_='a-last').find('a')  
#     next_page=('https://www.amazon.in'+page_nav.get('href'))  
#     print(next_page)
# # %%
