#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 23:12:05 2019

@author: calavera
"""
from urllib.request import Request, urlopen
import pandas as pd
import requests
import re

def url_to_html(url, headers):
    site = urlopen(Request(url, headers=headers))
    df = pd.read_html(site)
    return df

def scraperank(rankrange, rankweek):
    
    url = 'https://www.atptour.com/en/rankings/singles/?rankDate={0}&countryCode=all&rankRange=1-{1}'.format(rankweek, rankrange)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    df = url_to_html(url, hdr)
    df = df[0]
    df.Move = df.Move.fillna(0)
    df.Move = df.Move.apply(int)
    df.Ranking = df.Ranking.apply(lambda x: re.sub('T', '', x))
    df = df.drop('Country', axis=1)

    return df

def decurler(i):
    if type(i)==str: 
        i=re.sub('\(|\)','', i) 
    return i

#final_d['score'].apply(lambda x: re.sub(r'(76|67)(\d+ )', r'\1(2)', x))
 

