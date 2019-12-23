import pickle

import pandas as pd
import numpy as np
from flask import Flask, render_template
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from dao.artists_create import artists
import os
from dao.db import PostgresDb


db = PostgresDb()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "jkm-vsnej9l-vm9sqm3:lmve")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL",
                                                  "postgres://zsuiqzjfnryfqt:c15b2cf95d4adaf7477b92a3a51224ece7f0906d557f2bbd00c71226895040cb@ec2-174-129-32-240.compute-1.amazonaws.com:5432/dcku3qgnh2f0gf")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Year = []
Week_album = []
Week_population = []
Top_place = []
Average_orders = []

result = db.sqlalchemy_session.query(artists).all()
for row in result:
    Year.append(row.Year)
    Week_album.append(row.Week_album)
    Week_population.append(row.Week_population)
    Top_place.append(row.Top_place)
    Average_orders.append(row.Average_orders)
print('-----------------------------------------------')
print(len(Year), Year)
print(len(Week_album), Week_album)
print(len(Week_population), Week_population)
print(len(Top_place), Top_place)
print(len(Average_orders), Average_orders)
print('-----------------------------------------------')
X = pd.DataFrame(list(zip(Year, Week_album, Week_population, Top_place, Average_orders)),
                     columns=['Year', 'Week_album', 'Week_population', 'Top_place', 'Average_orders'])

y = pd.DataFrame(Week_population)
print('X_new', X)
print('Y_new', y)
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