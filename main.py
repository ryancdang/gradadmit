# Load libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

%matplotlib inline
pd.get_option('display.width')
pd.set_option('display.width', 120)
sns.set(rc={'figure.figsize':(12.7,8.27)})

data = pd.read_csv('Admission_Predict_Ver1.1.csv')

data.drop('Serial No.', inplace=True, axis=1)
data.rename({'Chance of Admit ': 'Chance of Admit', 'LOR ':'LOR'}, axis=1, inplace=True)
