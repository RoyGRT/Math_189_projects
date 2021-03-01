# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis, skew

data = pd.read_csv('babies23 (1).csv')

# %%
sns.set(style="white", rc={"axes.facecolor": 'white'})

# Birth weight in ounces vs. Smoking
non_smoke = data[data['time'] < 1]
smoke = data[(data['time'] >= 1) & (data['smoke'] < 9)]

non_smoke_weight = non_smoke['wt']
smoke_weight = smoke['wt']

fig, ax = plt.subplots()

sns.distplot(non_smoke_weight, kde=True, color='mediumblue', label='Non-Smoke')
sns.distplot(smoke_weight, kde=True, color='brown', label='Smoke')

plt.xlabel('Birth Weight')
plt.ylabel('Frequency')
plt.legend()
plt.title('Birth Weight for Smoking Mothers and Non-Smoking Mothers')

plt.show()

# %%

# Get summary statistics
print(f'Mean Birth Weight for Non-Smoking Mothers: {round(np.mean(non_smoke_weight), 2)}')
print(f'Mean Birth Weight for Smoking Mothers: {round(np.mean(smoke_weight), 2)}')

print(f'Median Birth Weight for Non-Smoking Mothers: {round(np.median(non_smoke_weight), 2)}')
print(f'Median Birth Weight for Smoking Mothers: {round(np.median(smoke_weight), 2)}')

print(f'Standard Deviation of Birth Weight for Non-Smoking Mothers: {round(np.std(non_smoke_weight), 2)}')
print(f'Standard Deviation of Birth Weight for Smoking Mothers: {round(np.std(smoke_weight), 2)}')

print(f'Skewness of Birth Weight for Non-Smoking Mothers: {round(skew(non_smoke_weight), 2)}')
print(f'Skewness of Birth Weight for Smoking Mothers: {round(skew(smoke_weight), 2)}')

print(f'Kurtosis of Birth Weight for Non-Smoking Mothers: {round(kurtosis(non_smoke_weight), 2)}')
print(f'Kurtosis of Birth Weight for Smoking Mothers: {round(kurtosis(smoke_weight), 2)}')

# %%

# Now, show the differences between weight based on when mother quit smoking
# For this, we should generate a "ridge line plot".

sns.set(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

data_plot = data[(data.time != 98) & (data.time != 99)]

pal = sns.cubehelix_palette(13, rot=-.25, light=.7)
g = sns.FacetGrid(data_plot, row='time', hue='time', aspect=15, height=.5,
                  palette=pal)

g.map(sns.kdeplot, 'wt',
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=1.5)
g.map(sns.kdeplot, 'time', clip_on=False, color='w', lw=2, bw_adjust=.5)
g.map(plt.axhline, y=0, lw=2, clip_on=False)


def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .4, label, fontweight='bold', color=color,
            ha='left', va='center', transform=ax.transAxes)


g.map(label, 'time')

g.set_titles("")
g.set(yticks=[])
g.set_xlabels('Birth Weight (oz)')
g.despine(bottom=True, left=True)
g.fig.suptitle('Birth Weight Distributions vs. Time of Mother Quitting Smoking')
plt.show()
