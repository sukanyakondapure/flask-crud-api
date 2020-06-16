from db import db
# from sqlalchemy_continuum import make_versioned
# from sqlalchemy import Column, Integer, Unicode, UnicodeText, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import create_session, configure_mappers

# Must be called before defining all the models
# make_versioned(user_cls=None)



class UserModel(db.Model):
    __tablename__ = 'users'
    __versioned__ = {}
     
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'username': self.username
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

