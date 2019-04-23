# Importing Modules and Reading the .csv File
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
#from plotly.offline import init_notebook_mode, iplot
#import cufflinks as cf

pd.get_option('display.width')
pd.set_option('display.width', 120)
sns.set(rc={'figure.figsize':(12.7,8.27)})

pd.options.mode.chained_assignment = None

data = pd.read_csv('Admission_Predict_Ver1.1.csv')
data.drop('Serial No.', inplace=True, axis=1)
data.rename({'Chance of Admit ': 'Chance of Admit', 'LOR ':'LOR'}, axis=1, inplace=True)

# Prediction Models

## Preparing the data
X = data.drop(['Chance of Admit'], axis=1)
y = data['Chance of Admit']

#Standardization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X[['CGPA','GRE Score', 'TOEFL Score']] = scaler.fit_transform(X[['CGPA','GRE Score', 'TOEFL Score']])

#Splitting
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=101)

# Linear Regression (All Features)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(X_train, y_train)
lr_predictions = lr.predict(X_test)

from sklearn.metrics import r2_score, mean_squared_error
lr_r2 = r2_score(y_test, lr_predictions)
lr_mse = mean_squared_error(y_test, lr_predictions)
lr_rmse = np.sqrt(lr_mse)

print('Linear Regression R2 Score: ' + str(lr_r2))
print('Linear Regression MSE: ' + str(lr_mse))
print('Linear Regression RMSE: ' + str(lr_rmse))
