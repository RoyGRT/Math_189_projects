import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from test_freqs import get_threshold

data = pd.read_csv('babies23 (1).csv')

rep = {'Low Weight': 0, 'Normal Weight': 1}

smoke_weight = data[data.time >= 1].wt
non_smoke_weight = data[data.time < 1].wt
df = get_threshold(88.2).replace(rep)

for thres in [
    65, 70, 75, 80, 85, 86, 87.5, 88.2, 90, 95, 100, 105, 115, 125, 135]:
    df = get_threshold(thres).replace(rep)
    contingency_tab = [
        [len(df[df['Smoke'] == 1.0]), len(df[df['Non-Smoke'] == 1.0])],
        [len(df[df['Smoke'] == 0.0]), len(df[df['Non-Smoke'] == 0.0])]]
    p = chi2_contingency(contingency_tab)[1]
    print(f'Thres: {thres}, p-value: {p}')