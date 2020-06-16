from db import db
from sqlalchemy_continuum import make_versioned, version_class, parent_class
import sqlalchemy as sa
from sqlalchemy import Column, Integer, Unicode, UnicodeText, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session, configure_mappers

# Must be called before defining all the models
make_versioned(user_cls=None)

Base = declarative_base()

class User_newModel(db.Model, Base):
    __tablename__ = 'user_new'
    __versioned__ = {}
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50))   
    email=db.Column(db.String(50),unique=True)
    mobile= db.Column(db.String(11)) 
    country_id=db.Column(db.Integer)
    state_id=db.Column(db.Integer)
    city_id=db.Column(db.Integer)
    hobbies=db.Column(db.String(255))
    gender=db.Column(db.Integer)
    address=db.Column(db.String(255))
    user_modified= db.Column(db.String(50))
    
    
    sa.orm.configure_mappers()

    
    def __init__(self, name, email, mobile, country_id, state_id, city_id, gender,hobbies, address, user_modified):                
        self.name = name
        self.email = email
        self.mobile = mobile
        self.country_id = country_id
        self.state_id = state_id
        self.city_id = city_id
        self.gender = gender
        self.hobbies = hobbies
        self.address = address
        self.user_modified = user_modified
    
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email':self.email,
            'mobile':self.mobile,
            'country_id':self.country_id,
            'state_id':self.state_id,
            'city_id':self.city_id,
            'gender':self.gender,
            'hobbies':self.hobbies,
            'address':self.address,
            'user_modified':self.user_modified
        }
    
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
     
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()    
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
sa.orm.configure_mappers()
engine = create_engine('postgresql://postgres:pqrs@localhost/application_db')
Base.metadata.create_all(engine)
session = create_session(bind=engine, autocommit=True)


    
    
