# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('dataset.csv')
X = dataset.iloc[:, 2:-1].values
y = dataset['price'].astype(str)
y = y.str.replace(',', '').str.replace('₹', '').astype(int)
Y = pd.DataFrame(y)

# Encoding categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
label_encoder = LabelEncoder()
X[: , 0] = label_encoder.fit_transform(X[: , 0])
X[: , 1] = label_encoder.fit_transform(X[: , 1])
X[: , 2] = label_encoder.fit_transform(X[: , 2])
X[: , 6] = label_encoder.fit_transform(X[: , 6])
X[: , 4] = label_encoder.fit_transform(X[: , 4])
X[: , 5] = label_encoder.fit_transform(X[: , 5])

#ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
#X = np.array(ct.fit_transform(X))
#print(X)

Y.dtypes

Y = Y.astype(int)

v = pd.DataFrame(X)

v.dtypes

v[0] = v[0].astype(int)
v[1] = v[1].astype(int)
v[2] = v[2].astype(int)
v[4] = v[4].astype(int)
v[5] = v[5].astype(int)
v[6] = v[6].astype(int)

v[3] = v[3].astype(str)
v[3] = v[3].str.replace(' ', '').str.replace('mm', '').astype(float)

v[7] = v[7].astype(str)
v[7] = v[7].str.replace(' ', '').str.replace('mm', '').astype(float)

v[8] = v[8].astype(str)
v[8] = v[8].str.replace(' ', '').str.replace('g', '').astype(float)

v[9] = v[9].astype(str)
v[9] = v[9].str.replace(' ', '').str.replace('mm', '').str.replace('cm', '').astype(float)

#creating backup
p = v

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(v, Y, test_size = 0.2, random_state = 0)

# Training the Multiple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

df = pd.DataFrame(columns = ['predicted_price', 'actual_price'])

df['actual_price'] = y_test['price']
df['predicted_price'] = y_pred
df.reset_index(drop=True, inplace=True)

df.to_csv('result.csv')
