#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: calavera
"""


from urllib.request import Request, urlopen
import pandas as pd
import requests
import re
#usate da pagina del torneo, esempio: https://www.atptour.com/en/scores/archive/doha/451/2019/results

def matchScraper(url):
    
    hdr = {'User-Agent': 'Mozilla/5.0'}
    site = urlopen(Request(url, headers=hdr))
    listaframe = pd.read_html(site)
    score = listaframe[0].dropna(1, thresh=2).dropna(0).set_index(0)
    score.index.name=''
    d = listaframe[1].set_index(2)
    d = d.dropna(0, thresh=2)
    d = d.dropna(1)
    dt = d.T
    dt = dt.set_index(score.index)
    dt = score.join(dt)
    dt.to_csv('laparta.csv', mode='a')
    
url = input('url')

reqtext = requests.get(url).text

urlspattern = re.compile('/en/scores/\d{4}.+match.+False')

path_list = re.findall(urlspattern, reqtext)

domain_name = 'https://www.atptour.com'

url_list = [domain_name+path for path in path_list]

for url in url_list:
    matchScraper(url)
