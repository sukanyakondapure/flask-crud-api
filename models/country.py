from db import db

class Countries(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50)) 

