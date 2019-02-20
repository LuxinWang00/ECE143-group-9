#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:23:22 2019

@author: Yudi Wang
"""
# In[1]
import requests
import re

def get_encoding(url, headers = None):
    """
    To get the website's endcoding from tag<meta content = 'UTF-8''>
    For each web, the encoding method keep identical, so we only need to consider the index page
    """
    res = requests.get(url, headers = headers)
    charset = re.search("charset = (.*?)>", res.text)
    if charset is not None:
        blocked = ['\'', ' ', '\"', '/']
        filter = [c for c in charset.group(1) if c not in blocked]
        return ''.join(filter)
    else:
        return res.encoding

# In[2]

import csv
import time
from lxml import etree

#setting up headers to mimic the normal request from users
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'
} 
encoding = get_encoding('https://opentrolley.com.sg/Home.aspx', headers) #'utf-8'

#list of web ready to scratch, 2o pages in total
urls = ['https://opentrolley.com.sg/Search.aspx?bestseller=fiction&page={}&pgsz=20'.format(i) for i in range(1,21)]

# From the list page
detail_url = []
name = []
author = []
price = []
# book_type = []

# From the detailed page
pages = []
publisher = []
# category = []

# In[3]

if __name__ == '__main__':
    # 20 pages in total
    for i in range(1):
        res = requests.get(urls[i], headers)
        #get the set-up user-agent
        res.encoding = encoding
        selector = etree.HTML(res.text)

        #pick up the 20 books in the page
        booklist = selector.xpath('//*[@id="ctl00_ContentPlaceHolder1_UpdatePanel1"]/div')
        book = [book for book in booklist]
        
        for i in range(len(book)):

            temp_link = book[i].xpath('div[2]/div[1]/a/@href')
            temp_link = 'https://opentrolley.com.sg/'+ temp_link[0]
            detail_url.append(temp_link) # detailed link
            name.append(book[i].xpath('div[2]/div[1]/a/text()')[0]) # name of the book       
            author.append(book[i].xpath('div[2]/div[2]/a[1]/text()'))  # author
            price.append(book[i].xpath("div[3]/div[3]/span[2]/text()")) #price
            time.sleep(0.5)
    
    # print (detail_url)
    # print (name)
    # print (author)
    # print (price)
    
    # go to the detailed page and obtained other information   
    for url in detail_url:
        res = requests.get(url, headers)
        res.encoding = encoding
        # pattern = '//*[@id="ctl00_ContentPlaceHolder1_UpdatePanel1"]/div/div[2]/div[1]/a/@href'
        # category.append(etree.HTML(res.text).xpath('//*[@id="ctl00_ContentPlaceHolder1_upcategoryname"]/div[1]/a[2]/text()'))
        pages.append(etree.HTML(res.text).xpath('//*[@id="ctl00_ContentPlaceHolder1_divBookDetail"]/div[2]/div[6]/div[2]/span/text()'))
        publisher.append(etree.HTML(res.text).xpath('//*[@id="ctl00_ContentPlaceHolder1_lblPublisher"]/text()')[0]) 
        time.sleep(0.5)


# print (category)
print (pages)
print (publisher)

# In[4]

output = open('/Users/yudiwang/Documents/19WinterECE143/Group Project/opentrolley/result.csv', 'w', encoding=encoding, newline='')  # put the message into the new .csv document
writer = csv.writer(output)  # csv writer
writer.writerow(('name', 'author', 'price', 'detail_url'))
for i in range(20*10):
    writer.writerow((name[i], author[i], price[i], detail_url[i]))  




                
            
    