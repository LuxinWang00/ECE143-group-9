#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:40:11 2019

@author: Yudi Wang
"""
#In [1]
import requests
import re
import csv
import time
from lxml import etree

def get_encoding(url, headers=None):   
    """
    :url: link need to be analyzied
    :headers: mimic the user's normal request
    To get the website's endcoding from tag<meta content = 'UTF-8''>
    For each web, the encoding method keep identical, so we only need to
    consider the index page
    """
    res = requests.get(url, headers=headers)
    charset = re.search("charset = (.*?)>", res.text)
    if charset is not None:
        blocked = ['\'', ' ', '\"', '/']
        filter = [c for c in charset.group(1) if c not in blocked]
        return ''.join(filter)
    else:
        return res.encoding
# In[2]
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
ori_price = []
publish_type = []
# From the detailed page
pages = []
publisher = []
num_available = []
publish_date = []
# 20 pages in total

if __name__ == '__main__':
    for p in range(10):
        print(p)
        res = requests.get(urls[p], headers)
        # Get the set-up user-agent
        res.encoding = encoding
        selector = etree.HTML(res.text)
    
        # Pick up the 20 books in the page
        booklist = selector.xpath('//*[@id="ctl00_ContentPlaceHolder1_UpdatePanel1"]/div')
        book = [book for book in booklist]       
        for i in range(len(book)):
    
            temp_link = book[i].xpath('div[2]/div[1]/a/@href')
            temp_link = 'https://opentrolley.com.sg/'+ temp_link[0]
            detail_url.append(temp_link) # detailed link
            name.append(book[i].xpath('div[2]/div[1]/a/text()')) # name of the book       
            author.append(book[i].xpath('div[2]/div[2]/a[1]/text()'))  # author
            ori_price.append(book[i].xpath('div[3]/div[2]/span[2]/text()')) # Original price between discount
            price.append(book[i].xpath("div[3]/div[3]/span[2]/text()")) # price
            publish_type.append(book[i].xpath('div[2]/div[3]/text()')) # publish type
            time.sleep(0.5)
    

    
        # go to the detailed page and obtained other information   
        for url in detail_url:
            res = requests.get(url, headers)
            res.encoding = encoding
            pages.append(etree.HTML(res.text).xpath('//*[@id="ctl00_ContentPlaceHolder1_divBookDetail"]/div[2]/div[6]/div[2]/span/text()')) # pages
            publisher.append(etree.HTML(res.text).xpath('//*[@id="ctl00_ContentPlaceHolder1_lblPublisher"]/text()')) # publisher
            num_available.append(etree.HTML(res.text).xpath('//*[@id="ctl00_ContentPlaceHolder1_lblstock"]/text()')) # available numbers
            publish_date.append(etree.HTML(res.text).xpath('//*[@id="ctl00_ContentPlaceHolder1_lblPublicationDate"]/text()')) # publish date
            time.sleep(0.5)
            
#         print (detail_url)
#         print (name)
#         print (author)
#         print (price)
#         print (ori_price)
#         print(publish_type)
#         print (pages)
#         print (publisher)
#         print(num_available)
#         print(publish_date)
#    
            
# In[3]          
#   Data pre-processing, abstract the meaningful information from the raw data
    name = [str(n) for n in name]
    author = [a[0].replace(' ', '')for a in author]
    price = [float(p[0]) for p in price]
    ori_price = [float(op[0]) for op in ori_price]
    pages = [int(p[0]) for p in pages]
    publish_date = [pd[0] for pd in publish_date]
    publish_type = [str(pt[0]).split()[0] for pt in publish_type]
    publish_type = [pt.replace('(', '')for pt in publish_type]
    
#    #existing the lack of data problem
#    num_available = [num[0].split()[0] for num in num_available] # To do
# 
# In[4]
    output = open('/Users/yudiwang/Documents/19WinterECE143/Group Project/opentrolley/Fiction_Result100.csv', 
                  'w', encoding=encoding, newline='')  # put the message into the new .csv document
    writer = csv.writer(output)  # csv writer
    writer.writerow(('name', 'author', 'price', 'original price',
                     'pages','publisher', 'publish type', 'publish date',
                     'available numbers',  'detail_url'))
    list_len = len(name)
    for i in range(list_len):
        writer.writerow((name[i], author[i], price[i], ori_price[i], pages[i], 
                        publisher[i], publish_type[i], publish_date[i],
                        num_available[i], detail_url[i]))







