import pandas as pd
import csv

# Target website: https://www.football-data.co.uk/data.php

df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')
print(df_premier21)

df_premier21.rename(columns={'HomeTeam': 'HOME', 'FTHG': 'home_goals', 'FTAG': 'away_goals'}, inplace=True)
print(df_premier21)
