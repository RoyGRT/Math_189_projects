# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from scipy.stats import poisson
from scipy.stats import skew

data = pd.read_csv('./datasets/hcmv.txt', sep='\n', header=None)
data = data.rename(columns=data.iloc[0]).drop(data.index[0]).astype(int)

# %%
n_pairs = 229354


def split_data(df, len_intervals):
    # 229,354 base pairs, 296 palindromes
    bins = []
    # labels = [i for i in range(int(n_pairs / len_intervals))]

    for i in range(0, n_pairs + len_intervals, len_intervals):
        bins.append(i + 1)

    header = 'binned_' + str(len_intervals)

    df[header] = pd.cut(df.location, bins)

    return df, 'Distribution of Palindromes for ' + str(
        int(n_pairs / len_intervals)) + ' Intervals'


# %%
def poisson_hist(len_intervals):
    d = split_data(data, len_intervals)[0]
    col = d['binned_' + str(len_intervals)]
    n_intervals = int(n_pairs / len_intervals)
    counts = col.value_counts().rename_axis('Counts').to_frame('Frequency')
    print(f'SKEW COUNT {n_intervals}: {skew(counts.Frequency)}')
    n, bins_edges, patches = plt.hist(counts, range(0, n_intervals), density=1, facecolor='black', log=0)
    lambd = counts.Frequency.mean()
    x_plot = range(0, n_intervals + 10)
    plt.axvline(lambd, color='r', alpha=0.5, linestyle='--', label='Mean')
    plt.plot(x_plot, poisson.pmf(x_plot, lambd), label='Poisson Distribution', color='blue')
    print(f'SKEW PMF {n_intervals}: {skew(poisson.pmf(x_plot, lambd))}')
    plt.title(split_data(data, len_intervals)[1])
    plt.legend()
    plt.xlabel('Bins')
    plt.xlim(0, 25)
    plt.ylabel('Frequency')
    plt.fill_between(x_plot, poisson.pmf(x_plot, lambd), alpha=0.5, color='blue')
    plt.show()
# %%
def resid(len_intervals):
    d = split_data(data, len_intervals)[0]
    col = d['binned_' + str(len_intervals)]
    n_intervals = int(n_pairs / len_intervals)
    counts = col.value_counts().rename_axis('Counts').to_frame('Frequency')
    lambd = counts.Frequency.mean()
    x_plot = range(0, n_intervals + 1)
    p = poisson.pmf(x_plot, lambd)
    resids = np.abs(counts.Frequency - p)
    resids = (resids - np.mean(resids)) / np.std(resids)
    return resids.values, n_intervals


# %%
len_intervals = [11467, 9174, 4587, 3058, 2293, 1529]
for l in len_intervals:
    plt.scatter(range(3, len(resid(l)[0])), resid(l)[0][3:], s=2.5, color='black')
    plt.title('Pearson Standardized Residuals for ' + str(resid(l)[1]) + ' Intervals')
    plt.show()
