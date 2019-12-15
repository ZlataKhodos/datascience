import numpy

import pandas as pd
import numpy as np
import pylab
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

dataset = pd.read_csv('artists.csv')
dataset.head()

X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 2].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

regressor = RandomForestRegressor(n_estimators=200, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

print('y_pred = ', y_pred)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


X_list = list(X[:,0])
y_list = list(y)

plt.scatter(X_list, y_list)
plt.show()

# Visualising the Random Forest Regression results 

# arange for creating a range of values 
# from min value of x to max 
# value of x with a difference of 0.01 
# between two consecutive values 
X_grid = np.arange(min(numpy.array(X[:,0])), max(numpy.array(X[:,0])), 0.01) 

# reshape for reshaping the data into a len(X_grid)*1 array, 
# i.e. to make a column out of the X_grid value				 

# Scatter plot for original data 
plt.scatter(list(X[:,0]), list(y), color = 'blue') 

# plot predicted data 
plt.plot(X_grid.reshape((len(X_grid), 1)) , regressor.predict(X_grid.reshape((len(X_grid), 1)) ), 
		color = 'green') 
plt.title('Random Forest Regression') 
plt.xlabel('Position level') 
plt.ylabel('Salary') 
plt.show()

