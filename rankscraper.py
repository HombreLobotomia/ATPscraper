
from datetime import date
import pandas as pd
from urllib.request import Request, urlopen

urlpath = 'https://www.atptour.com/en/rankings/singles/?rankDate=2019-4-8&countryCode=all&rankRange=1-'
rankrange = str(input('enter range')) 
url = urlpath + rankrange
hdr = {'User-Agent': 'Mozilla/5.0'}
site = urlopen(Request(url, headers=hdr))
df = pd.read_html(site)
df = df[0]
df.Move = df.Move.fillna(0)
df.Move = df.Move.apply(int)
df = df.drop('Country', axis=1)
date  =  str(date.today())
df.to_csv('ATP_top_'+rankrange+'_'+date+'.csv')