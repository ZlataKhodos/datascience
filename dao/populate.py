from dao.artists_create import *
from dao.db import PostgresDb

db = PostgresDb()

Base.metadata.create_all(db.sqlalchemy_engine)
session = db.sqlalchemy_session
session.query(artists).delete()

add_data = [['2002', '34', '42', '1', '541'], ['2002', '41', '48', '7', '524'], ['2002', '33', '40', '9', '561'], ['2002', '38', '45', '13', '414'], ['2002', '15', '20', '17', '410'], ['2002', '24', '29', '20', '344'], ['2002', '19', '26', '2', '544'], ['2003', '41', '48', '5', '467'], ['2003', '14', '17', '9', '464'], ['2003', '25', '30', '7', '498'], ['2003', '4', '9', '3', '580'], ['2003', '12', '18', '8', '471'], ['2003', '17', '23', '4', '525'], ['2003', '27', '31', '6', '508'], ['2004', '42', '48', '6', '566'], ['2004', '18', '23', '3', '635'], ['2004', '26', '31', '4', '603'], ['2004', '37', '42', '1', '865'], ['2004', '46', '51', '2', '865'], ['2004', '31', '34', '7', '640'], ['2004', '3', '8', '10', '549'], ['2005', '43', '50', '2', '650'], ['2005', '17', '21', '9', '464'], ['2005', '28', '31', '7', '547'], ['2005', '10', '16', '8', '460'], ['2005', '31', '36', '5', '566'], ['2005', '24', '27', '4', '577'], ['2005', '36', '41', '3', '631'], ['2005', '40', '44', '6', '574'], ['2006', '36', '40', '10', '534'], ['2006', '34', '39', '6', '571'], ['2006', '23', '26', '8', '554'], ['2006', '30', '34', '5', '577'], ['2006', '37', '41', '3', '628'], ['2006', '28', '31', '13', '487'], ['2006', '12', '17', '1', '644'], ['2006', '40', '46', '2', '640'], ['2007', '37', '40', '4', '704'], ['2007', '35', '39', '7', '648'], ['2007', '43', '49', '1', '968'], ['2007', '49', '55', '12', '587'], ['2007', '26', '30', '5', '699'], ['2007', '11', '16', '8', '632'], ['2007', '17', '21', '10', '591'], ['2007', '22', '29', '3', '782'], ['2008', '31', '33', '8', '510'], ['2008', '46', '49', '3', '610'], ['2008', '13', '17', '7', '524']]
# with open('artists.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         add_data.append(row)
# add_data.pop(0)
# print(add_data)

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

# print(len(ident), ident)
# print(len(Year), Year)
# print(len(Week_album), Week_album)
# print(len(Week_population), Week_population)
# print(len(Top_place), Top_place)
# print(len(Average_orders), Average_orders)

data_to_add = []

for i in range (len(ident)):
    data_to_add.append(artists(id=ident[i], Year=Year[i], Week_album=Week_album[i],
                               Week_population=Week_population[i], Top_place=Top_place[i],
                               Average_orders=Average_orders[i]))
session.add_all(data_to_add)
session.commit()