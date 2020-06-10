from app import db


class Area(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Area = db.Column (db.String(20), nullable=False, unique=True)
    principales = db.relationship('Principal', backref='area', lazy=True)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column (db.String(10), unique=True)
    Ubicacion = db.Column (db.String(10))
    principales = db.relationship('Principal', backref='cliente', lazy=True)    

class Principal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nroticket = db.Column (db.Integer, unique=True, nullable=False )
    detalle = db.Column (db.String(50), nullable=False )
    fecha = db.Column (db.String(8), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'),
        nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'),
        nullable=False)    