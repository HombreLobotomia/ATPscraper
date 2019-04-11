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



#df2 = df.loc[df['winner_name'] == df['loser_name']]
#len(set(players[i]))==len(players)

