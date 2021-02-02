import pandas as pd

url = 'https://en.wikipedia.org/wiki/World_Series'

world_series = pd.read_html(url, attrs={'class':'multicol'})[0]
world_series = world_series.iloc[2:32]
world_series.columns = ['Team', 'Series Wins', 'Series Played', 'Last Won', 'Last Played']
world_series = world_series.reset_index(drop=True)
print(world_series)

