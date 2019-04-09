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
    
    site = urlopen(Request(url, headers=hdr))
    listaframe = pd.read_html(site)
    score = listaframe[0].dropna(1, thresh=2).dropna(0).set_index(0)
    #score.index.name=''
    first_score_name = score.index[0].split(' ')[-1]
    d = listaframe[1].set_index(2)
    d = d.dropna(0, thresh=2)
    d = d.dropna(1)
    dt = d.T
    dt_rows = dt.values.tolist()
    if first_score_name in df2[gen[i]]:    
        dt_rows = dt_rows[0]+dt_rows[1]
    else:
                dt_rows = dt_rows[0]+dt_rows[1]

    df2[gen[i]]=df2[gen[i]]+dt_rows
    #dt = dt.set_index(score.index)
    
    #dt = score.join(dt)
    #dt.to_csv('laparta.csv', mode='a')
    
url = input('url')

reqtext = requests.get(url).text
hdr = {'User-Agent': 'Mozilla/5.0'}
site = urlopen(Request(url, headers=hdr))
urlspattern = re.compile('/en/scores/\d{4}.+match.+False')
path_list = re.findall(urlspattern, reqtext)
domain_name = 'https://www.atptour.com'
url_list = [domain_name+path for path in path_list]

listaframe = pd.read_html(site)
df=listaframe[2]
df = df.drop(['Unnamed: 3','Unnamed: 8', 'Unnamed: 9', 'Unnamed: 1', 'Unnamed: 5'], axis=1)
df.columns=['winner_seed', 'winner', 'loser_seed', 'loser', 'score']
df2 = df.values.tolist()
gen = [df2.index(i) for i in df2 if '(W/O)' not in i]

for i in range(len(url_list)):
    matchScraper(url_list[i])

final_d = pd.DataFrame(df2)
final_d.columns=['winner_seed', 'winner', 'loser_seed', 'loser', 'score', 'Serve Rating', 'Aces', 'Double Faults', '1st Serve',
       '1st Serve Points Won', '2nd Serve Points Won', 'Break Points Saved',
       'Service Games Played', 'Return Rating', '1st Serve Return Points Won',
       '2nd Serve Return Points Won', 'Break Points Converted',
       'Return Games Played', 'Service Points Won', 'Return Points Won',
       'Total Points Won', 'Serve Rating', 'Aces', 'Double Faults', '1st Serve',
       '1st Serve Points Won', '2nd Serve Points Won', 'Break Points Saved',
       'Service Games Played', 'Return Rating', '1st Serve Return Points Won',
       '2nd Serve Return Points Won', 'Break Points Converted',
       'Return Games Played', 'Service Points Won', 'Return Points Won',
       'Total Points Won']
final_d.to_csv('torneo.csv')