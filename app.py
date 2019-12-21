import pickle

import numpy

import pandas as pd
import numpy as np
import pylab
from flask import Flask, jsonify
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

app = Flask(__name__)

dataset = pd.read_csv('artists.csv')
dataset.head()

X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 2].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
filename = 'finalized_model.pkl'

@app.route('/', methods=['POST'])
def predict():

    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.score(X_test, y_test)
    print(result)
    output = {'results': result}
    #return output
    # return data
    return jsonify(results=output)

#print(predict())

if __name__ == '__main__':
    app.run()
#
# X_list = list(X[:,0])
# y_list = list(y)
#
# plt.scatter(X_list, y_list)
# plt.show()

# Visualising the Random Forest Regression results 

# arange for creating a range of values 
# from min value of x to max 
# value of x with a difference of 0.01 
# between two consecutive values 
# X_grid = np.arange(min(numpy.array(X[:,0])), max(numpy.array(X[:,0])), 0.01)

# reshape for reshaping the data into a len(X_grid)*1 array, 
# i.e. to make a column out of the X_grid value				 

# Scatter plot for original data 
# plt.scatter(list(X[:,0]), list(y), color = 'blue')

# plot predicted data 
# plt.plot(X_grid.reshape((len(X_grid), 1)) , regressor.predict(X_grid.reshape((len(X_grid), 1)) ),
# 		color = 'green')
# plt.title('Random Forest Regression')
# plt.xlabel('Position level')
# plt.ylabel('Salary')
# plt.show()

