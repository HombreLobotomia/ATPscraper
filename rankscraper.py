from datetime import datetime, timedelta
import pandas as pd
from urllib.request import Request, urlopen
import re

def scraperank(rankrange, rankweek):
    
    url = 'https://www.atptour.com/en/rankings/singles/?rankDate={0}&countryCode=all&rankRange=1-{1}'.format(rankweek, rankrange)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    site = urlopen(Request(url, headers=hdr))
    df = pd.read_html(site)
    df = df[0]
    df.Move = df.Move.fillna(0)
    df.Move = df.Move.apply(int)
    df = df.drop('Country', axis=1)
    df.to_csv('ATP_top_{0}_{1}.csv'.format(rankrange, rankweek))

rankrange = input('enter range')
rankweek = input('enter week: format YYYY-MM-DD')
rankweek = datetime.strptime(rankweek, '%Y-%m-%d').date()
weekdays = int(rankweek.weekday())
rankweek = rankweek - timedelta(days=weekdays)
rankweek = re.sub('-0', '-', str(rankweek))

scraperank(rankrange, rankweek)

