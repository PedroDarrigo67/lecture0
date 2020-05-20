from flask import Flask, render_template, request, url_for
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
    id = 1
    nickname = Principal.query.filter_by(id=id).first() 
    Prin_id = nickname.id
    Prin_ticket = str(nickname.nroticket)
    Prin_detalle = nickname.detalle
    Prin_fecha = nickname.fecha
    Prin_area_id = nickname.area_id
    Prin_cliente_id = nickname.cliente_id
    return render_template("Vista.html", Prin_id = Prin_id, Prin_ticket = Prin_ticket, Prin_detalle = Prin_detalle, Prin_fecha = Prin_fecha, Prin_area_id = Prin_area_id, Prin_cliente_id = Prin_cliente_id )

@app.route("/button")
def Proxima():
    max_count = 4
    count = 2

    nickname = Principal.query.filter_by(id=2).first() 
    Prin_id = nickname.id
    Prin_ticket = str(nickname.nroticket)
    Prin_detalle = nickname.detalle
    Prin_fecha = nickname.fecha
    Prin_area_id = nickname.area_id
    Prin_cliente_id = nickname.cliente_id
    return render_template("Vista.html", Prin_id = Prin_id, Prin_ticket = Prin_ticket, Prin_detalle = Prin_detalle, Prin_fecha = Prin_fecha, Prin_area_id = Prin_area_id, Prin_cliente_id = Prin_cliente_id )
 



@app.route("/login", methods=["GET", "POST"])
def login():
    user = Principal.query.filter_by(detalle=request.form["nickname"]).first()
    return render_template("login.html")









@app.route("/insert/default")
def insert_default():
    new_client = Principal(nroticket=4, detalle="detalle 4", fecha="12-05-20", area_id=2, cliente_id=2)
    db.session.add(new_client)
    db.session.commit()
    return "Se cargo area" 




 
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)