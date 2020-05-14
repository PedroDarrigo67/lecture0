from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 
 
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



@app.route("/")
def Inicio():
    return render_template("Index.html")


@app.route("/Index.html")
def Index():
    return render_template("Index.html")
    
    


@app.route("/Generar_ticket.html")
def Generar():
    return render_template("Generar_ticket.html") 

@app.route("/Vista.html")
def Vista():
    Prinfecha = "12-05-20"
    Printicket = "ticket1"
    return render_template("Vista.html", Prinfecha = Prinfecha, Printicket = Printicket)     


@app.route("/insert/default")
def insert_default():
    new_client = Principal(nroticket=4, detalle="detalle 4", fecha="12-05-20", area_id=2, cliente_id=2)
    db.session.add(new_client)
    db.session.commit()
    return "Se cargo area" 




 
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)