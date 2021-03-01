import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportion_confint


# %%

video = pd.read_csv('datasets/video.csv')
time = video.time
prop = len(time[time > 0]) / len(time)  # 0.3736

# %%

sns.displot(video, x='time')
plt.xlabel('Time (Hr.)')
plt.ylabel('Frequency')
plt.title('Hours Playing Video Games Week Prior to Survey')
plt.axvline(x=np.mean(time), color='r')
plt.axvline(x=np.median(time), color='r', linestyle='--')
plt.show()

print(len(time[time > 0]))
print(len(time))


# %%

proportion_confint(34, 91, 0.05)
