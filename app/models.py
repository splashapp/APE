from . import db

class Faehigkeit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    beschreibung = db.Column(db.Text)
    link = db.Column(db.String(200))