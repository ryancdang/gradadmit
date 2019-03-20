# Load libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# matplotlib inline
pd.get_option('display.width')
pd.set_option('display.width', 120)
sns.set(rc={'figure.figsize':(12.7,8.27)})

# Load dataset
data = pd.read_csv('Admission_Predict_Ver1.1.csv')

data.drop('Serial No.', inplace=True, axis=1)
data.rename({'Chance of Admit ': 'Chance of Admit', 'LOR ':'LOR'}, axis=1, inplace=True)

## Head of the data
data.head()

## General statistics of the data
data.describe()

## Correlation coefficients
data.corr()

## Correlation coefficients heatmap
sns.heatmap(data.corr(), annot=True).set_title('Correlation Factors Heat Map', color='black', size='30')

# Isolating GRE Score data
GRE = pd.DataFrame(data['GRE Score'])
GRE.describe()

# Probability Distribution
sns.distplot(GRE).set_title('Probability Distribution for GRE Test Scores', size='30')
plt.show()

# Correlation Coeffecients for GRE Score Test
GRE_CORR = pd.DataFrame(data.corr()['GRE Score'])
GRE_CORR.drop('GRE Score', axis=0, inplace=True)
GRE_CORR.rename({'GRE Score': 'GRE Correlation Coeff'}, axis=1, inplace=True)
GRE_CORR

# Isolating and describing TOEFL Score
TOEFL = pd.DataFrame(data['TOEFL Score'], columns=['TOEFL Score'])
TOEFL.describe()

# Probability distribution for TOEFL Scores
sns.distplot(TOEFL).set_title('Probability Distribution for TOEFL Scores', size='30')
plt.show()

# Isolating and describing the CGPA
CGPA = pd.DataFrame(data['CGPA'], columns=['CGPA'])
CGPA.describe()

RES_Count = data.groupby(['Research']).count()
RES_Count = RES_Count['GRE Score']
RES_Count = pd.DataFrame(RES_Count)
RES_Count.rename({'GRE Score': 'Count'}, axis=1, inplace=True)
RES_Count.rename({0: 'No Research', 1:'Research'}, axis=0, inplace=True)
plt.pie(x=RES_Count['Count'], labels=RES_Count.index, autopct='%1.1f%%')
plt.title('Research', pad=5, size=30)
plt.show()

# Isolating and describing 
University_Rating = data.groupby(['University Rating']).count()
University_Rating = University_Rating['GRE Score']
University_Rating = pd.DataFrame(University_Rating)
University_Rating.rename({'GRE Score': 'Count'}, inplace=True, axis=1)
University_Rating

# Barplot for the distribution of the University Rating
sns.barplot(University_Rating.index, University_Rating['Count']).set_title('University Rating', size='30')
plt.show()

#Isolating and describing
SOP = pd.DataFrame(data.groupby(['SOP']).count()['GRE Score'])
SOP.rename({'GRE Score':'Count'}, axis=1, inplace=True)
SOP

# Barplot for SOP 
sns.barplot(SOP.index, SOP['Count']).set_title('Statement of Purpose', size='30')
plt.show()

# Isolating and describing
LOR = pd.DataFrame(data.groupby(['LOR']).count()['GRE Score'])
LOR.rename({'GRE Score':'Count'}, axis=1, inplace=True)
LOR

# Distribution of the LOR
sns.barplot(LOR.index, LOR['Count']).set_title('Letter of Recommendation', size='30')
plt.show()

data['Chance of Admit']
sns.distplot(data['Chance of Admit']).set_title('Probability Distribution of Chance of Admit', size='30')
plt.show()

data.describe()['Chance of Admit']

COA_corr = pd.DataFrame(data.corr()['Chance of Admit'])
COA_corr.rename({'Chance of Admit': 'Correlation Coeffecient'}, axis=1, inplace=True)
COA_corr.drop('Chance of Admit', inplace=True)
COA_corr.sort_values(['Correlation Coeffecient'], ascending=False, inplace=True)
COA_corr_x = COA_corr.index
COA_corr_y = COA_corr['Correlation Coeffecient']
sns.barplot(y=COA_corr_x,x=COA_corr_y).set_title('Chance of Admit Correlation Coeffecients', size='30')
plt.show()

COA_corr

X = data[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research']]
y = data['Chance of Admit']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.33, random_state=42)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

coeff = pd.DataFrame(lm.coef_, X.columns, columns=['Coeffecients'])
coeff

print("Intercept : ",lm.intercept_)

sns.scatterplot(y_test, predictions)
plt.ylabel("Predictions")
plt.xlabel("Actual Value")
plt.show()

residuals = y_test - predictions
sns.distplot(residuals)
plt.xlabel("Residuals")
plt.ylabel("Probability")
plt.show()
plt.show()

from sklearn import metrics
MAE = metrics.mean_absolute_error(y_test, predictions)
MSE = metrics.mean_squared_error(y_test, predictions)
RMSE = np.sqrt(MSE)
R_squared = metrics.r2_score(y_test, predictions)
pd.DataFrame(data=[MAE, MSE, RMSE, R_squared], index=['MAE', 'MSE', 'RMSE', 'R Squared'], columns=['Value'])

# Preparing the testing data
X = X[['CGPA', 'GRE Score', 'TOEFL Score']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
lm2 = LinearRegression()
lm2.fit(X_train, y_train)
predictions2 = lm2.predict(X_test)

# Getting the results
coeff2 = pd.DataFrame(lm2.coef_, index=X_train.columns, columns=['Coeffecients'])
coeff2

print("Intercept: ", lm2.intercept_)

residuals2 = y_test - predictions2
sns.distplot(residuals2)
plt.xlabel("Residuals")
plt.ylabel("Probability")
plt.show()

MAE = metrics.mean_absolute_error(y_test, predictions2)
MSE = metrics.mean_squared_error(y_test, predictions2)
RMSE = np.sqrt(MSE)
R_squared = metrics.r2_score(y_test, predictions2)
pd.DataFrame(data=[MAE, MSE, RMSE, R_squared], index=['MAE', 'MSE', 'RMSE', 'R Squared'], columns=['Value'])

print("Mean for Chance of Admit: ", data['Chance of Admit'].mean())

from sklearn.linear_model import LogisticRegression 
lr = LogisticRegression()

# Adjust the data
X = data[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research']]
y_logistic = data['Chance of Admit'].copy()
y_logistic.replace(to_replace=y[y >= 0.72],value=1, inplace=True)
y_logistic.replace(to_replace=y[y < 0.72], value=0, inplace=True)
X_train, X_test, y_train, y_test = train_test_split(X, y_logistic, test_size=0.3, random_state=42)

from sklearn import preprocessing
lr.fit(X_train, y_train)
predictions = lr.predict(X_test)

print(metrics.classification_report(y_test, predictions))

print("Accuracy: ", metrics.accuracy_score(y_test, predictions))

# Prepare the data by standardizing it
features = data[['GRE Score', 'TOEFL Score', 'CGPA']]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(features)
scaled_features = scaler.transform(features)
X = pd.DataFrame(scaled_features, columns=features.columns)

X_train, X_test, y_train, y_test = train_test_split(X,y_logistic,test_size=0.3, random_state=101)

from sklearn.neighbors import KNeighborsClassifier
accuracy = []
for i in range (1,40):
    classifier = KNeighborsClassifier(n_neighbors=i)
    classifier.fit(X_train, y_train)
    predictions = classifier.predict(X_test)
    accuracy.append(metrics.accuracy_score(y_test, predictions))
    

plt.plot(range(1,40), accuracy, linestyle='dashed', marker='o', markersize=10, markerfacecolor='red')
plt.xlabel('K Value')
plt.ylabel('Accuracy')
plt.title('K Value vs Accuracy')
plt.show()

K = accuracy.index(np.max(accuracy)) + 1
print("Best K Value: ", K)

KNN = KNeighborsClassifier(n_neighbors=K)
KNN.fit(X_train, y_train)
predictions = KNN.predict(X_test)

print(metrics.classification_report(y_test, predictions))