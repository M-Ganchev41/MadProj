import os
from sqlalchemy import Boolean, Integer, create_engine, MetaData, Table, Column, String, Float, ForeignKey, Date
from databases import Database

#DATABASE_URI = "mysql+pymysql://root:admin@127.0.0.1:3306/car_rental"
DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata=MetaData()

car = Table(
    'car', metadata,
    Column('carID', Integer, primary_key=True),
    Column('availability', Boolean),
    Column('colour', String(31)),
    Column('power', Integer),
    Column('makeFK_ID', Integer, ForeignKey('make.makeID')),
    Column('description', String(255))
)

make = Table(
    'make', metadata,
    Column('makeID', Integer, primary_key=True),
    Column('makeName', String(31)),
    Column('modelFK_ID', Integer, ForeignKey('model.modelID'))
)

model = Table(
    'model', metadata,
    Column('modelID', Integer, primary_key=True),
    Column('modelName', String(31))
)

subscription = Table(
    'subscription', metadata,
    Column('subscriptionID', Integer, primary_key=True),
    Column('subscriptionStartDate', Date),
    Column('subscriptionEndDate', Date),
    Column('subscriptionDailyPrice', Float),
    Column('carFK_ID', Integer, ForeignKey('car.carID')),
    Column('userFK_ID', Integer, ForeignKey('users.userID'))
)

users = Table(
    'users', metadata,
    Column('userID', Integer, primary_key=True),
    Column('firstName', String(31)),
    Column('lastName', String(31)),
    Column('roleFK_ID', Integer, ForeignKey('roles.roleID'))
)

roles = Table(
    'roles', metadata,
    Column('roleID', Integer, primary_key=True),
    Column('roleName', String(31))
)

database = Database(DATABASE_URI)