from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fähigkeit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    beschreibung = db.Column(db.String(255), nullable=True)

class Anwendung(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    leanix_id = db.Column(db.String(100), nullable=False)
    einzelrechte = db.relationship('Einzelrecht', backref='anwendung', lazy=True)
    anwendungsrollen = db.relationship('Anwendungsrolle', backref='anwendung', lazy=True)
    it_bundles = db.relationship('ITBundle', backref='anwendung', lazy=True)

class Einzelrecht(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    beschreibung = db.Column(db.String(255), nullable=True)
    privilegiert = db.Column(db.Boolean, default=False)
    sod_area = db.Column(db.String(100), nullable=True)
    bestellbar = db.Column(db.Boolean, default=True)
    anwendung_id = db.Column(db.Integer, db.ForeignKey('anwendung.id'), nullable=False)
    anwendungsrollen = db.relationship('Anwendungsrolle', secondary='einzelrecht_anwendungsrolle', lazy='subquery', backref=db.backref('einzelrechte', lazy=True))
    it_bundles = db.relationship('ITBundle', secondary='einzelrecht_itbundle', lazy='subquery', backref=db.backref('einzelrechte', lazy=True))

class Anwendungsrolle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    beschreibung = db.Column(db.String(255), nullable=True)
    anwendung_id = db.Column(db.Integer, db.ForeignKey('anwendung.id'), nullable=False)
    it_bundles = db.relationship('ITBundle', secondary='anwendungsrolle_itbundle', lazy='subquery', backref=db.backref('anwendungsrollen', lazy=True))

class ITBundle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    beschreibung = db.Column(db.String(255), nullable=True)
    privilegiert = db.Column(db.Boolean, default=False)
    sod_area = db.Column(db.String(100), nullable=True)
    bestellbar = db.Column(db.Boolean, default=True)
    anwendung_id = db.Column(db.Integer, db.ForeignKey('anwendung.id'), nullable=False)

einzelrecht_anwendungsrolle = db.Table('einzelrecht_anwendungsrolle',
    db.Column('einzelrecht_id', db.Integer, db.ForeignKey('einzelrecht.id'), primary_key=True),
    db.Column('anwendungsrolle_id', db.Integer, db.ForeignKey('anwendungsrolle.id'), primary_key=True)
)

einzelrecht_itbundle = db.Table('einzelrecht_itbundle',
    db.Column('einzelrecht_id', db.Integer, db.ForeignKey('einzelrecht.id'), primary_key=True),
    db.Column('itbundle_id', db.Integer, db.ForeignKey('itbundle.id'), primary_key=True)
)

anwendungsrolle_itbundle = db.Table('anwendungsrolle_itbundle',
    db.Column('anwendungsrolle_id', db.Integer, db.ForeignKey('anwendungsrolle.id'), primary_key=True),
    db.Column('itbundle_id', db.Integer, db.ForeignKey('itbundle.id'), primary_key=True)
)