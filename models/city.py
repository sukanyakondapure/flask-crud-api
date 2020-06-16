# from db import db 

class Cities(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50)) 
    state_id=db.Column(db.Integer)