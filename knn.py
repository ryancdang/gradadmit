# Load libraries
import pandas as pd


data = pd.read_csv('Admission_Predict_Ver1.1.csv')

data.drop('Serial No.', inplace=True, axis=1)
data.rename({'Chance of Admit ': 'ChanceofAdmit', 'LOR ':'LOR'}, axis=1, inplace=True)

## Data has 500 rows and 8 columns, after erasing serial number
#print(data.head())

X=data.iloc[:, 0:7].values
#X is the attributes
y=data.iloc[:, 7].values
#Y is the label
#print(X)
#print(y)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


from sklearn.linear_model import LinearRegression
clf = LinearRegression();
results = clf.fit(X_train, y_train).predict(X_test);
print(results[len(results) -1])