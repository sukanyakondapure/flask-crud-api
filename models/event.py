from db import db
# import sqlalchemy as sa
# from sqlalchemy_continuum import make_versioned
# from sqlalchemy import Column, Integer, Unicode, UnicodeText, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import create_session, configure_mappers

# Must be called before defining all the models
# make_versioned(user_cls=None)

# Base = declarative_base()

class Event(db.Model):
    __tablename__ = 'events'
    # __versioned__ = {}  # Must be added to all models that are to be versioned
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # name = sa.Column(sa.String)
	# start_time = sa.Column(db.DateTime, nullable=False)
    # end_time = sa.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text)
    schedule_published_on = db.Column(db.DateTime)
    
    # Must be called after defining all the models
# sa.orm.configure_mappers()