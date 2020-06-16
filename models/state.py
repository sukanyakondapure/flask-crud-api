# from db import db

class States(db.Model):
    __tablename__ = 'state'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50)) 
    country_id=db.Column(db.Integer)

