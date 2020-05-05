from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 

class Principal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nro_ticket = db.Column (db.Integer, unique=True, nullable=False )
    detalle = db.Column (db.String(50), nullable=False )
    fecha = db.Column (db.String(8), nullable=False)
    Area = db.relationship (db.Integer, backref = 'principal', lazy = True)
    Cliente = db.relationship (db.Integer, backref = 'principal', lazy = True)
    
    
class Area(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Area = db.Column (db.String(10), nullable=False)
    id_principal = db.Column(db.Integer, db.ForeignKey('principal.id'), nullable=False)
    

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Nombre = db.Column (db.String(10))
    Ubicacion = db.Column (db.String(10))
    id_principal = db.Column(db.Integer, db.ForeignKey('principal.id'), nullable=False)



@app.route("/")
def index():
    return "Inicio"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)