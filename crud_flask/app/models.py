from app import db

class Movie(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    year = db.Column(db.String(64), index=True, nullable=False)
    gender = db.Column(db.String(64), index=True, nullable=False)

