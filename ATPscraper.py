import pandas as pd
import requests
import re
#   https://www.atptour.com/en/scores/archive/madrid/309/1975/results
#   https://www.atptour.com/en/scores/archive/cordoba/9158/2019/results
#   https://www.atptour.com/en/scores/archive/doha/451/2019/results

class scrapeObject:
    def __init__(self, url):
        self.url = url
        self.html = requests.get(self.url).text
        self.to_df = pd.read_html(self.html)
        
tourney = scrapeObject(input('url'))
dfs = tourney.to_df
df  = dfs[2]
df = df.drop(df.columns[[1,3,5,8,9]], axis=1)
df =  df.values.tolist()
gen = [df.index(i) for i in df if '(W/O)' not in i]

domain_name = 'https://www.atptour.com'
#player_pattern=re.compile('/en/players.+overview')
#players_list = set(re.findall(player_pattern, tourney.html))

urlspattern = re.compile('/en/scores/\d{4}.+match.+False')
path_list = re.findall(urlspattern, tourney.html)
matchlist = (domain_name+i for i in path_list)


for i in gen:
    match = scrapeObject(next(matchlist)).to_df
    time=[match[0][4][2]]
    match_stats = match[1]
    match_stats = match_stats.drop(match_stats.columns[[1,2,3]], axis=1)
    match_stats = match_stats.drop([8,14])
    match_stats = match_stats.T.values
    match_stats = match_stats.tolist()
    if  df[i][1] in match[0][0][2]:        
        df[i] += time+match_stats[0]+match_stats[1]
    else:
        df[i] += time+match_stats[1]+match_stats[0]


df = pd.DataFrame(df)

#'Serve Rating', 'Aces', 'Double Faults', '1st Serve',
#       '1st Serve Points Won', '2nd Serve Points Won', 'Break Points Saved',
#       'Service Games Played', 'Return Rating', '1st Serve Return Points Won',
#       '2nd Serve Return Points Won', 'Break Points Converted',
#       'Return Games Played', 'Service Points Won', 'Return Points Won',
#       'Total Points Won'

df.columns=['winner_seed', 'winner', 'loser_seed', 'loser', 'score', 'duration', 
#       winner_stats
       'w_sr', 'w_aces', 'w_df', 'w_1st_in', 'w_1st_svp', 'w_2nd_svp', 'w_bps', 'w_sgp', 
       'w_rr', 'w_1sts_rpw', 'w_2nds_rpw', 'w_bpc','w_rgp', 'w_spw', 'w_rpw','w_tpw', 
#       loser_stats
       'l_sr', 'l_aces', 'l_df', 'l_1st_in', 'l_1st_svp', 'l_2nd_svp', 'l_bps', 'l_sgp', 
       'l_rr', 'l_1sts_rpw', 'l_2nds_rpw', 'l_bpc','l_rgp', 'l_spw', 'l_rpw','l_tpw']

surface = dfs[0][1][0]
draw_size = dfs[0][0][0].split('  ')[1]
tourney_ID = tourney.url.split('/')[-3]
df.insert(0, 'tourney_ID', tourney_ID)
df.insert(1, 'tourney_name', dfs[0][1][1].split('  ')[0])
df.insert(2, 'surface', dfs[0][1][0])
df.insert(3, 'draw_size', draw_size)
df.insert(4, 'tourney_date', dfs[0][1][1].split('  ')[-1])   

df.to_csv('torneo.csv')
#('{0}-{1}.csv'.format(tourney_name, tourney_year))


