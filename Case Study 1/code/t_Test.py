import pandas as pd
from scipy import stats
from test_freqs import get_threshold

data = pd.read_csv('babies23 (1).csv')

rep = {'Low Weight': 0, 'Normal Weight': 1}

smoke_weight = data[data.time >= 1].wt
non_smoke_weight = data[data.time < 1].wt
df = get_threshold(88.2).replace(rep)

print(stats.ttest_ind(
    df['Smoke'].dropna(), df['Non-Smoke'].dropna(),
    equal_var=False, alternative='less'))

print(len(df['Smoke'].dropna()))
print(len(df['Non-Smoke'].dropna()))