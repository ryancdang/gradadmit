
import pandas as pd
import numpy as np

df = pd.read_csv('Admission_Predict_Ver1.1.csv')
df = df.rename(columns={'Chance of Admit ': 'ChanceOfAdmit'})

# Now i'm doing the correlation between all the columns
import matplotlib.pyplot as plt
import seaborn as sns
fig,ax = plt.subplots(figsize=(9, 9))
sns.heatmap(df.corr(), ax=ax, annot=True, linewidths=0.05, fmt='.2g', cmap="YlGnBu")
#plt.show()
#from the figure above we can get to the conclusion that the three best options
#to be used as labels in our model are: CGPA, GRE and TOEFL

#Lets check out if this is true with PCA
