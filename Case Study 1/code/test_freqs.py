import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('babies23 (1).csv')

smoke_weight = data[data.time >= 1]
non_smoke_weight = data[data.time < 1]


def get_threshold(threshold):
    bins = [0, threshold, np.inf]
    names = ['Low Weight', 'Normal Weight']

    smoke_weight_thres = pd.cut(
        smoke_weight.wt.rename('Smoke'), bins, labels=names)
    non_smoke_weight_thres = pd.cut(
        non_smoke_weight.wt.rename('Non-Smoke'), bins, labels=names)

    res = pd.concat([smoke_weight_thres, non_smoke_weight_thres], axis=1)
    return res


def plot_threshold(thres, threshold):
    fig, ax = plt.subplots(1, 2, sharey=True)
    sns.countplot(data=thres, x='Smoke', palette='BrBG',
                  edgecolor='black', ax=ax[0])
    ax[0].set_ylabel('Number of Babies')
    sns.countplot(data=thres, x='Non-Smoke', palette='BrBG',
                  edgecolor='black', ax=ax[1])
    ax[1].set_ylabel('')
    ax[1].tick_params(left=False, bottom=True)
    sns.despine(fig=None, ax=ax[0], top=True, right=True, left=False,
                bottom=True, offset=None, trim=False)
    sns.despine(fig=None, ax=ax[1], top=True, right=True, left=True,
                bottom=True, offset=None, trim=False)
    fig.suptitle('Occurrences of Low and Normal Birth Weights for Smoking'
                 ' and Non-Smoking Mothers \n(Threshold = {} Oz.)'.format(
        threshold), fontsize=10)

    plt.show()


if __name__ == '__main__':
    for thres in [
        65, 70, 75, 80, 85, 86, 87.5, 88.2, 90, 95, 100, 105, 115, 125, 135]:
        srs = get_threshold(thres)
        for status in ['Smoke', 'Non-Smoke']:
            curr = srs[status].dropna()
            print(f'{status}: Low weight '
                  f'proportion for {thres}'
                  f': {round(len(curr[curr == "Low Weight"]) / len(curr), 3)}')
        plot_threshold(srs, thres)
