import pandas as pd
import numpy as np
data = pd.read_csv("C:\\Personal\\Data\\scores.csv")

#function to label bars in the barplots
def barlabel(b, i):
    for bar in bars:
        height = bar.get_height()
        ax[i].text(bar.get_x()+bar.get_width()/2., 0.90*height, 
            '%d' % int(height), color='white', ha='center', va='bottom')

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
