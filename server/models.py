from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)

    animals = db.relationship('Animal', back_populates='zookeeper')

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)
    
    animals = db.relationship('Animal', back_populates='enclosure')

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id')) 
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    
    enclosure = db.relationship('Enclosure', back_populates='animals')
    zookeeper = db.relationship('Zookeeper', back_populates='animals')
