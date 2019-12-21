import pickle

import pandas as pd
import numpy as np
from flask import Flask, render_template
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
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

filename = 'finalized_model.pkl'
pickle.dump(regressor, open(filename, 'wb'))

# some time later...

# load the model from disk
@app.route('/')
def predict():
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.score(X_test, y_test)
    print(result)
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run()