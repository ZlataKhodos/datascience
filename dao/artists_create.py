from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

class artists(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    Year = Column(Integer)
    Week_album = Column(Integer)
    Week_population = Column(Integer)
    Top_place = Column(Integer)
    Average_orders = Column(Integer)