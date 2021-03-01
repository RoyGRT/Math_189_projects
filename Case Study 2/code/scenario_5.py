import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from scipy.stats import chi2_contingency

#%%
video = pd.read_csv('../datasets/video.csv')

like = video[(video.like == 2) | (video.like == 3)]
dislike = video[(video.like != 2) & (video.like != 3)]

video['like_video_games'] = video.like.apply(
    lambda x: 'yes' if x == 2 or x == 3 else 'no')
video['sex'] = video.sex.apply(
    lambda x: 'female' if x == 0 else 'male')

like_and_sex = pd.crosstab(video.sex, video.like_video_games)
sns.heatmap(like_and_sex, linewidths=0.5,
            annot=True, cmap='gist_gray')

plt.title('Sex vs. Video Game Preference')
plt.show()

#%%
chi2_contingency(like_and_sex)
#%%
sns.distplot(video.work[video.work != 99], kde=False)
plt.axvline(np.mean(video.work), color='red', label='Mean')
plt.axvline(np.median(video.work), color='black', label='Median')
plt.legend()
plt.title('Distribution of Hours Worked Week Prior to Survey')
plt.xlabel('Hours')
plt.ylabel('Frequency')
plt.show()

#%%
video['work_sched'] = video.work.apply(
    lambda x: 'unemployed' if x == 0 else('part-time' if (x > 0 and x < 30) else 'full-time'))

like_and_work = pd.crosstab(video.work_sched, video.like_video_games)
sns.heatmap(like_and_work, linewidths=0.5,
            annot=True, cmap='gist_gray')

plt.title('Work Schedule vs. Video Game Preference')
plt.show()

#%%
chi2_contingency(like_and_work)
#%%
like_and_computer = pd.crosstab(video.home, video.like_video_games)
sns.heatmap(like_and_computer, linewidths=0.5,
            annot=True, cmap='gist_gray')

plt.title('Computer Ownership vs. Video Game Preference')
plt.show()
#%%
sns.countplot(video.home, palette='hls')
plt.title('Computer Ownership')
plt.xlabel('Computer Ownership (0=No, 1=Yes)')
plt.ylabel('Count')
plt.show()
#%%
chi2_contingency(like_and_computer)