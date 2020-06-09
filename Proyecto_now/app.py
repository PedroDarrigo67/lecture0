from flask import Flask, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 

Prin_id_lista = ['PR']
Prin_nroticket_lista = [1]
Prin_detalle_lista = ['PR']
Prin_fecha_lista = ['PR']
Prin_area_id_lista = [1]
Prin_cliente_id_lista = [1]

movreg = 1
sumreg = 6

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
    success_index = 'Bienvenido'
    flash(success_index) 
    return render_template("Index.html")

@app.route("/Vista.html")
def Vista():
    global movreg 
    global sumreg
    movreg = 1
    sumreg = db.session.query(Principal).count()
    if Prin_id_lista[0] == 'PR': 
        Prin_id_lista.remove('PR')
        Prin_nroticket_lista.remove(1)
        Prin_detalle_lista.remove('PR')
        Prin_fecha_lista.remove('PR')
        #Prin_area_id_lista.remove = (1)
        #Prin_cliente_id_lista.remove = (1)
        movreg = 1
    while movreg < sumreg + 1:
        nickname = Principal.query.filter_by(id=movreg).first()
        
        Prin_id_lista.insert(movreg, nickname.id)
        Prin_nroticket_lista.insert(movreg, nickname.nroticket)
        Prin_detalle_lista.insert(movreg, nickname.detalle)
        Prin_fecha_lista.insert(movreg, nickname.fecha)

        area_vis = Area.query.filter_by(id=nickname.area_id).first()
        Prin_area_id_lista.insert(nickname.area_id, area_vis.Area)

        cliente_vis = Cliente.query.filter_by(id=nickname.cliente_id).first()
        Prin_cliente_id_lista.insert(nickname.cliente_id, cliente_vis.Nombre)

        movreg = movreg + 1
    return render_template("Vista.html", sumreg = sumreg, Prin_id_lista = Prin_id_lista, Prin_nroticket_lista = Prin_nroticket_lista, Prin_detalle_lista=Prin_detalle_lista, Prin_fecha_lista=Prin_fecha_lista, Prin_area_id_lista=Prin_area_id_lista, Prin_cliente_id_lista=Prin_cliente_id_lista)


@app.route("/Generar", methods=["GET", "POST"])
def nuevo1():
    return render_template("Generar.html") 

@app.route("/Generar.html", methods=["GET", "POST"])
def nuevo():
    global sumreg
    sumreg = db.session.query(Principal).count()
    sumreg = sumreg + 1
    if request.method == "POST":
        detalles = request.form["detalle"]
        fechas = request.form["fecha"]
        nroticket = 1000 + sumreg
        areas = request.form["area"]

        clientes = request.form["cliente"]


        new_client = Principal(nroticket=nroticket, detalle=detalles, fecha=fechas, area_id=areas, cliente_id=clientes)
        db.session.add(new_client)
        db.session.commit()
        success_messages = 'Genero el ticket exitosamente ' + str(nroticket)
        flash(success_messages) 
       
    return render_template("Generar.html") 

@app.route("/Editar.html")
def editar():
    global movreg 
    global sumreg
    sumreg = db.session.query(Principal).count()
    movreg = 1
    nickname = Principal.query.filter_by(id=movreg).first() 
    Prin_id = nickname.id
    Prin_ticket = str(nickname.nroticket)
    Prin_detalle = nickname.detalle
    Prin_fecha = nickname.fecha
    Prin_area = Area.query.filter_by(id=nickname.area_id).first()
    Prin_area_id = Prin_area.Area

    Prin_cliente = Cliente.query.filter_by(id=nickname.cliente_id).first()
    Prin_cliente_id = Prin_cliente.Nombre

    return render_template("Editar.html", Registros = sumreg, Prin_id = Prin_id, Prin_ticket = Prin_ticket, Prin_detalle = Prin_detalle, Prin_fecha = Prin_fecha, Prin_area_id = Prin_area_id, Prin_cliente_id = Prin_cliente_id )

@app.route("/button")
def editar1():
    global movreg 
    global sumreg
    botones = request.args.get('boton')
    if botones == "adelante":
        movreg = movreg + 1
        if movreg > sumreg:
            movreg = sumreg
    else:  
        movreg = movreg - 1
        if movreg == 0:
            movreg = 1  
    nickname = Principal.query.filter_by(id=movreg).first()
    Prin_id = nickname.id
    Prin_ticket = str(nickname.nroticket)
    Prin_detalle = nickname.detalle
    Prin_fecha = nickname.fecha

    Prin_area = Area.query.filter_by(id=nickname.area_id).first()
    Prin_area_id = Prin_area.Area

    Prin_cliente = Cliente.query.filter_by(id=nickname.cliente_id).first()
    Prin_cliente_id = Prin_cliente.Nombre     



    return render_template("Editar.html", Registros = sumreg, Prin_id = Prin_id, Prin_ticket = Prin_ticket, Prin_detalle = Prin_detalle, Prin_fecha = Prin_fecha, Prin_area_id = Prin_area_id, Prin_cliente_id = Prin_cliente_id )
 
app.secret_key = "9495"
 
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)