
from scraping_functions import *

import json
url = 'https://www.atptour.com/en/scores/archive/cordoba/9158/2019/results'
f = json.load(open('ATP_players.json'))
hdr = {'User-Agent': 'Mozilla/5.0'}
df = url_to_html(url, hdr)
reqtext = requests.get(url).text
players_list = set(re.findall('/en/players.+overview', reqtext))
keylist = [ i.split('/')[-2] for i in players_list]
nameslist = [ i.split('/')[-3] for i in players_list]
nameslist = [re.sub('-', ' ', i).title() for i in nameslist]
domain_name = 'https://www.atptour.com'
url_list = [domain_name+i for i in players_list]
df2=url_to_html(url_list[4], hdr)
#reqtext2 = requests.get(url_list[2]).text

p_age = df2[0][0][0][-11:-1]
p_pro = int(df2[0][1][0][-4:])
p_weight = int(df2[0][2][0][-5:-3])
p_height = int(df2[0][3][0][-6:-3])
p_h = df2[0][2][1][7]
p_bh = df2[0][2][1][-19]
player_values = [p_age, p_pro, p_weight, p_height, p_h, p_bh]
if keylist[2] not in f:
    f[nameslist[4]+'/'+keylist[4]]=player_values
json.dump(f, open("ATP_players.json",'w'))
#https://www.atptour.com/en/players/francisco-cerundolo/c0au/overview
