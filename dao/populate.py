import csv
from dao.artists_create import *
from dao.db import PostgresDb

db = PostgresDb()

Base.metadata.create_all(db.sqlalchemy_engine)
session = db.sqlalchemy_session
session.query(artists).delete()

add_data = []
with open('../artists.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        add_data.append(row)
add_data.pop(0)
print(add_data)

add_data_correct = []

for i in range (len(add_data)):
    for j in range (len(add_data[i])):
        add_data_correct.append(int(add_data[i][j]))
print(add_data_correct)

ident = [i for i in range(len(add_data))]
Year = []
Week_album = []
Week_population = []
Top_place = []
Average_orders = []

for i in range (len(add_data_correct)):
    if i%5==0:
        Year.append(add_data_correct[i])
    elif i%5==1:
        Week_album.append(add_data_correct[i])
    elif i%5==2:
        Week_population.append(add_data_correct[i])
    elif i%5==3:
        Top_place.append(add_data_correct[i])
    elif i%5==4:
        Average_orders.append(add_data_correct[i])
    else:
        print('something went wrong')

print(len(ident), ident)
print(len(Year), Year)
print(len(Week_album), Week_album)
print(len(Week_population), Week_population)
print(len(Top_place), Top_place)
print(len(Average_orders), Average_orders)

data_to_add = []

for i in range (len(ident)):
    data_to_add.append(artists(id=ident[i], Year=Year[i], Week_album=Week_album[i],
                               Week_population=Week_population[i], Top_place=Top_place[i],
                               Average_orders=Average_orders[i]))
session.add_all(data_to_add)
session.commit()