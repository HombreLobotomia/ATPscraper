import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
#from collections import Counter
df = pd.read_csv('csvs/atpdata.csv')
#namesid = pd.concat([df.winner_id.apply(str)+'/'+df.winner_name, df.loser_id.apply(str)+'/'+df.loser_name])
#namesid = namesid.drop_duplicates()
#namesidlisted = namesid.str.split('/')
#names = [i[1]  for i in namesidlisted]
#conta = Counter(names)

players = pd.read_csv('csvs/atp_players.csv', encoding='latin_1',  header=None, names=['player_id', 'last_name', 'name', 'hand', 'iGuessAge?', 'ioc'] )
#players[1] = players[1]+' '+players[2]
#players=players.drop(2, axis=1)



(df.loser_age, df.winner_age) = (df.loser_age.fillna(0), df.winner_age.fillna(0))
(df.loser_age, df.winner_age) = ((df.loser_age.apply(lambda x: round(x, 3)), df.winner_age.apply(lambda x: round(x, 4))))
(df.loser_age, df.winner_age) = (df.loser_age.replace(0, np.NaN), df.winner_age.replace(0, np.NaN))
df.tourney_date = pd.to_datetime(df.tourney_date, format='%Y%m%d')

#assert players['player_id'].notnull().all() 
#assert players[1].notnull().all()
dfrecent = df.loc[df['tourney_date'] > pd.to_datetime('2008/12/31')]   
dfrecent = dfrecent.loc[dfrecent['round']=='F']
dfrecent.plot(x='tourney_date', y='winner_age')
plt.show()
#!! Quite surprisingly, that's not the case: tons of missing values even in players names

match_stat_columns=['w_ace', 'w_df', 'w_svpt', 'w_1stIn', 'w_1stWon',
       'w_2ndWon', 'w_SvGms', 'w_bpSaved', 'w_bpFaced', 'l_ace', 'l_df',
       'l_svpt', 'l_1stIn', 'l_1stWon', 'l_2ndWon', 'l_SvGms', 'l_bpSaved',
       'l_bpFaced']
winner_stats = match_stat_columns[:9]
loser_stats = match_stat_columns[9:]
b=df.loc[df.index==168618]
b=b[match_stat_columns]
#npb=np.array(b)
size = 0.5
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))
fig1, ax1 = plt.subplots()
winstats=b[winner_stats].T
losestats=b[loser_stats].T
ax1.pie(winstats, colors=outer_colors, radius=1, wedgeprops=dict(width=size, edgecolor='w'))
ax1.pie(losestats, colors=inner_colors, radius=1-size, wedgeprops=dict(width=size, edgecolor='w'))
plt.show()
#df2 = df.loc[df['winner_name'] == df['loser_name']]
#len(set(players[i]))==len(players)

ax=plt.subplot(projection='polar')
bars=ax.bar(winner_stats, 3)
ax=plt.subplot(projection='polar')
cars=ax.bar(loser_stats, 3)
for r, bar in zip(bars, cars):
    bar.set_facecolor(plt.cm.viridis(cars/10.))
plt.show()