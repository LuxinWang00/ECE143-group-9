#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:28:21 2019

@author: yudiwang
"""
# In[]
import pandas as pd
import os
#import csv



data_file = []
class_name = []
path = "/Users/yudiwang/Documents/19WinterECE 143/Group Project/opentrolley/Data"
all_category = '/Users/yudiwang/Documents/19WinterECE 143/Group Project/opentrolley/Data/all_category.csv'
#header_all = ['name', 'author', 'price', 'original price', 'pages', 'publisher',
#       'publish type', 'publish date', 'available numbers', 'detail_url',
#       'Category']
#with open(all_category,'wb') as outcsv:
#    writer = csv.writer(outcsv)
#    writer.writerow(header_all)
#outcsv.close()
# Read all the csv document
for dirpath, dirnames, filenames in os.walk(path):
        for name in filenames:
            if '.csv' in name:
                data_file.append(os.path.join(dirpath, name))
                # Figure out the category tag
                tmp = os.path.splitext(name)[0]
                class_name.append(([k.strip() for k in tmp.split('_')][0]).capitalize())

# In[]:
for i in range(len(data_file)):
#for i in range(2):
    # Load the csv document
    data_tmp = pd.read_csv(data_file[i])
    # Add the category
    data_tmp['Category'] = class_name[i]
    # Cut out the tail
    tail_len = len(data_tmp)-190
    tmp_frame = data_tmp.drop(data_tmp.tail(tail_len).index)
    # Do data cleaning, remove the empty number with 0
    avail_num = tmp_frame['available numbers'][:]
    for j in range(len(avail_num)):
        if avail_num[j] != '[]':
            avail_num[j]= avail_num[j].split()[0].replace("['","")
            avail_num[j] = int(avail_num[j])
        else:
            # Replace the empty string into 0
            avail_num[j] = 0
    tmp_frame['available numbers'] = avail_num  
    if i == 0:
        # For first document, keep the header
        tmp_frame.to_csv(all_category,encoding="utf_8_sig",index=False)
    else:  
        # For the latter dataset, drop the header
        tmp_frame.to_csv(all_category,encoding="utf_8_sig",index=False, header=False,mode='a+')
