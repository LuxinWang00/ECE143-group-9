# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:13:42 2019

@author: justi
"""

from pyquery import PyQuery as pq
import pandas as pd

#%%
url = "https://www.amazon.com/gp/bestsellers/2019/books/ref=zg_bsar_cal_ye"
def Top_Sells(url):
    html_doc = pq(url)
    
    Title = [x.text for x in html_doc("a-link-normal")]
    Title = [i.replace('\n','').replace('\t','') for i in Title]
    Arthur = [y.text for y in html_doc(".a-link-normal+ .a-size-small .a-size-small")]
    Arthur = [i.replace('\n','').replace('\t','') for i in Arthur]
    Price = [x.text for x in html_doc(".p13n-sc-price")]
    Price = [i.replace('\n','').replace('\t','').replace('$','') for i in Price]
    Review = [x.text for x in html_doc(".a-size-small.a-link-normal")]
    Review = [i.replace('\n','').replace('\t','') for i in Review]
    Review.insert(13,'none')
    
    
    return Title, Arthur, Price, Review

Title, Arthur, Price, Review = Top_Sells(url)
#Title = Title(url)
#%%
Books = pd.DataFrame()
Books["Title"] = Title
Books["Arthur"] = Arthur
Books["Price"] = Price
Books["Review"] = Review
Books.head()