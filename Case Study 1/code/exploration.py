import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import kurtosis

data = pd.read_csv("babies23 (1).csv")
non_smoke = data[data['smoke'] < 1]
smoker = data[data['smoke'] >= 1]
filtered_smoker = smoker[smoker['smoke'] < 9]

smoke_weight = filtered_smoker['wt']
non_smoke_weight = non_smoke['wt']

light_smoker = data[data['number'] <= 4]
light = light_smoker[light_smoker['number'] > 0]

heavy_smoker = data[data['number'] > 4]
heavy = heavy_smoker[heavy_smoker['number'] < 9]

#mean, median, std. dev
print("light smoker mean: " + str(np.mean(light['wt'])))
print("heavy smoker mean: " + str(np.mean(heavy['wt'])))

print("light smoker median: " + str(np.median(light['wt'])))
print("heavy smoker median: " + str(np.median(heavy['wt'])))

print("light smoker std. deviation: " + str(np.std(light['wt'])))
print("heavy smoker std. deviation: " + str(np.std(heavy['wt'])))

print("Kurtosis heavy-smoker: " + str(kurtosis(heavy['wt'])))
print("Kurtosis light-smoker: " + str(kurtosis(light['wt'])))

#Boxplot of smoking & non-smoking mothers
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

ax1.set_title('Non-Smoking Mothers')
non_smoke_df = pd.DataFrame(non_smoke_weight)
reset_non_smoke_df = non_smoke_df.reset_index()
del reset_non_smoke_df['index'] 
sns.boxplot(data = non_smoke_df, ax = ax1)

ax2.set_title('Smoking Mothers')
smoke_df = pd.DataFrame(smoke_weight)
reset_smoke_df = smoke_df.reset_index()
del reset_smoke_df['index'] 
sns.boxplot(data = reset_smoke_df, ax = ax2,color = 'indianred')

#QQPlot Against Normal for Smoking
stats.probplot(smoke_weight,dist="norm",plot=plt)
plt.title("Q-Q Plot of Birth Weights of Babies Born to Smoking Mothers")
plt.ylabel("Observed Quantiles")
plt.xlabel("Theoretical Quantiles")
plt.show()

#QQPlot Against Normal for Non-smoking
stats.probplot(non_smoke_weight,dist="norm",plot=plt)
plt.title("Q-Q Plot of Birth Weights of Babies Born to Non-Smoking Mothers")
plt.ylabel("Observed Quantiles")
plt.xlabel("Theoretical Quantiles")
plt.show()