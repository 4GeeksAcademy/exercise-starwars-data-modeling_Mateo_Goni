import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    subscription_date = Column(Integer, nullable=False)
    favorites = relationship('Favorites', back_populates='user')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    eyes_color = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users', back_populates='favorites')
class Favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    id= Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    favorites = relationship('Favorites', back_populates='favorites_planets')
    planets = relationship('Planets')

class Favorites_characters(Base):
    __tablename__ = 'favorites_characters'
    id= Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    favorites = relationship('Favorites', back_populates='favorites_characters')
    characters = relationship('Characters')

class Favorites_vehicles(Base):
    __tablename__ = 'favorites_vehicles'
    id= Column(Integer, primary_key=True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    favorites = relationship('Favorites', back_populates='favorites_vehicles')
    vehicles = relationship('Vehicles')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
