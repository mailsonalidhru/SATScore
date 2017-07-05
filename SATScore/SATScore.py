##### Import Libraries Section #####
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##### Variables Initialization #####
data = pd.read_csv("C:\\Personal\\Data\\scores.csv")

##### Processing Section #####
print('Highest average SAT Math score {} Lowest score {}.'.format(
      int(data['Average Score (SAT Math)'].max()), int(data['Average Score (SAT Math)'].min())))
print('\t')
print('Highest average SAT Reading score {} Lowest Score {}.'.format(
      int(data['Average Score (SAT Reading)'].max()), int(data['Average Score (SAT Reading)'].min())))
print('\t')
print('Highest average SAT Writing score {} Lowest {}.'.format(
      int(data['Average Score (SAT Writing)'].max()), int(data['Average Score (SAT Writing)'].min())))

print("Best School with Overall Average SAT Math Score {}.".format(
      data.loc[data['Average Score (SAT Math)']==754, 'School Name'].values[0]))
print('\t')
print("Worst School with Overall Average SAT Math Score {}".format(
      data.loc[data['Average Score (SAT Math)']==317, 'School Name'].values[0]))

print("Best School with Overall Average SAT Reading Score {}.".format(
      data.loc[data['Average Score (SAT Reading)']==697, 'School Name'].values[0]))
print('\t')
print("Worst School with Overall Average SAT Reading Score {}".format(
      data.loc[data['Average Score (SAT Reading)']==302, 'School Name'].values[0]))

print("Best Shool with Overall Average SAT Writing Score {}.".format(
      data.loc[data['Average Score (SAT Writing)']==693, 'School Name'].values[0]))
print('\t')
print("Worst School with Overall Average SAT Writing Score was {}".format(
      data.loc[data['Average Score (SAT Writing)']==284, 'School Name'].values[0]))

#### Label Bars in the Barplots
def barlabel(b, i):
    for bar in bars:
        height = bar.get_height()
        ax[i].text(bar.get_x()+bar.get_width()/2., 0.90*height, 
            '%d' % int(height), color='white', ha='center', va='bottom')

fig, ax = plt.subplots(3, figsize=(8, 12))
ind = np.arange(5)
width = 0.35
bars = ax[0].bar((ind+width), data.groupby('Borough')['Average Score (SAT Math)'].max())
ax[0].set_facecolor("white")
ax[0].set_title("Max Average SAT Math Score by Borough (2014-2015)", fontsize=18)
ax[0].set_xlabel('')
ax[0].set_xticks(ind+width/1.0)
ax[0].set_xticklabels(labels=data.groupby('Borough')['Average Score (SAT Math)'].max().index)
ax[0].set_yticklabels("")
barlabel(bars, 0)
bars[1].set_color('#f45c42')
bars[2].set_color('#41f4d9');


bars = ax[1].bar((ind+width), data.groupby('Borough')['Average Score (SAT Reading)'].max())
ax[1].set_facecolor("white")
ax[1].set_title("Max Average SAT Reading Score by Borough (2014-2015)", fontsize=18)
ax[1].set_xlabel('')
ax[1].set_xticks(ind+width/1.0)
ax[1].set_xticklabels(labels=data.groupby('Borough')['Average Score (SAT Reading)'].max().index)
ax[1].set_yticklabels("")
barlabel(bars, 1)
bars[1].set_color('#f45c42')
bars[2].set_color('#41f4d9')


bars = ax[2].bar((ind+width), data.groupby('Borough')['Average Score (SAT Writing)'].max())
ax[2].set_facecolor("white")
ax[2].set_title("Max Average SAT Writing Score by Borough (2014-2015)", fontsize=18)
ax[2].set_xlabel('')
ax[2].set_xticks(ind+width/1.0)
ax[2].set_xticklabels(labels=data.groupby('Borough')['Average Score (SAT Writing)'].max().index)
ax[2].set_yticklabels("")
barlabel(bars, 2)
bars[1].set_color('#f45c42')
bars[2].set_color('#41f4d9')

plt.tight_layout();
plt.show();

