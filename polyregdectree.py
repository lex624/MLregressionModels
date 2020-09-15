# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#fitting the decision tree to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

#Prediction for the test results
#y_pred = regressor.predict(np.array([6.5]).reshape(-1,1))
#y_pred = y.inverse_transform(regressor.predict(X.transform(np.array([6.5]))))
#y_pred = regressor.predict(X.transform([[6.5]]))
y_pred = regressor.predict(np.array([[5]]))

#plot the graph trained set
# plt.scatter(X, y, color = 'red')
# plt.plot(X, regressor.predict(X), color = 'blue')
# plt.title('Truth or Bluff (Decision Tree Regression)')
# plt.xlabel('Position Level')
# plt.ylabel('Salary')
# plt.show()

X_grid = np.arange(min(X), max(X), 0.01 )
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()



