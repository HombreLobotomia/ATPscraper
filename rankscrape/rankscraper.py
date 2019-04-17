from datetime import datetime, timedelta
from scraping_functions import *

rankrange = input('enter range')
rankweek = input('enter week: format YYYY-MM-DD')
rankweek = datetime.strptime(rankweek, '%Y-%m-%d').date()
weekdays = int(rankweek.weekday())
rankweek = rankweek - timedelta(days=weekdays)
rankweek = re.sub('-0', '-', str(rankweek))

rank = scraperank(rankrange, rankweek)

rank.to_csv('ATP_top_{0}_{1}.csv'.format(rankrange, rankweek))
