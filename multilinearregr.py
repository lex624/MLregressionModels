# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#cathegorise the non numeric variables
#Encoding categorical values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
LabelEncoder_X = LabelEncoder()
X[:, 3] = LabelEncoder_X.fit_transform(X[:, 3])
columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [3])],     
                                      remainder='passthrough')
X=np.float64(columnTransformer.fit_transform(X),dtype=np.str)

#avoiding the dummy variable trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#fitting multiple linear reg into the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Prediction for the test results
y_pred = regressor.predict(X_test)

#building optimal model using BACKWARD ELIMINATION
#import statsmodels.formula.api as sm
#X = np.append (arr =  np.ones((50,1).astype(int),values = X , axis = 1)

import statsmodels.api as sm
X = np.append(arr = np.ones((50, 1)).astype(int) , values = X, axis = 1)
X_opt = X[:, [0 ,1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0 ,1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0 , 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0 , 3, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0 , 3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()