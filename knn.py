# Load libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('Admission_Predict_Ver1.1.csv')

data.drop('Serial No.', inplace=True, axis=1)
data.rename({'Chance of Admit ': 'ChanceofAdmit', 'LOR ':'LOR'}, axis=1, inplace=True)

## Data has 500 rows and 8 columns, after erasing serial number
print(data.head())

#create a dataframe with all training data except the target column
X = data.drop(columns=["ChanceofAdmit"])
#check that the target variable has been removed
print(X.head())

#separate target values
y = data["ChanceofAdmit"].values
#view target values
#print(y[0:5])

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np
from sklearn                        import metrics, svm
from sklearn.linear_model           import LogisticRegression
from sklearn import preprocessing
from sklearn import utils
#split dataset into train and test data
#test size 0.2 means that 20% of the data will be used for testing
#stratify option is to keep the same proportion of chanceofadmit in the test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

from sklearn.neighbors import KNeighborsClassifier
# Create KNN classifier
#CHANGE THE K to the best number as we calculated before
lab_enc = preprocessing.LabelEncoder()
training_scores_encoded = lab_enc.fit_transform(y_train)
#print(training_scores_encoded)

knn = KNeighborsClassifier(n_neighbors=13)
knn.fit(X_train, training_scores_encoded)
print("K Nearest Neighbor /n")
print(knn.predict(y[len(y) - 1]))