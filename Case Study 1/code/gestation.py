# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

data = pd.read_csv('babies23 (1).csv')
data = data[data.time <= 9]

gestation_smoke = data[data['time'] >= 1].gestation
gestation_non_smoke = data[data['time'] < 1].gestation

gestation_smoke = gestation_smoke[gestation_smoke < 500]
gestation_non_smoke = gestation_non_smoke[gestation_non_smoke < 500]

sns.distplot(gestation_non_smoke, kde=True, bins=10, color='forestgreen', label='Non-Smoke')
sns.distplot(gestation_smoke, kde=True, bins=10, color='brown', label='Smoke')

plt.xlabel('Gestational Age')
plt.ylabel('Frequency')
plt.legend()
plt.title('Gestational Age for Smoking Mothers and Non-Smoking Mothers')
plt.show()

data = data[data.gestation < 500]

bins = [-1, 0, np.inf]
names = ['Non-Smoke', 'Smoke']
data.time = pd.cut(data.time, bins=bins, labels=names)

print(data.time)

sns.scatterplot(data=data, x='wt', y='gestation', hue='time', palette='CMRmap')
plt.legend(title='')
plt.title('Birth Weight vs. Gestational Age')
plt.xlabel('Birth Weight (oz.)')
plt.ylabel('Gestational Age (Days)')
plt.show()

# %%
print(stats.ttest_ind(
    gestation_smoke, gestation_non_smoke,
    equal_var=False, alternative='less'))