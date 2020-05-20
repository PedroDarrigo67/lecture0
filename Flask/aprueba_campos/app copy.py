from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 

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
    return render_template("Index.html")
    

@app.route("/Vista.html")
def Vista():
    global movreg 
    global sumreg
    sumreg = db.session.query(Principal).count()
    movreg = 1
    
    nickname = Principal.query.filter_by(id=movreg).first() 
    Prin_id = nickname.id
    Prin_ticket = str(nickname.nroticket)
    Prin_detalle = nickname.detalle
    Prin_fecha = nickname.fecha
    Prin_area_id = nickname.area_id
    Prin_cliente_id = nickname.cliente_id
    return render_template("Vista.html", Registros = sumreg, Prin_id = Prin_id, Prin_ticket = Prin_ticket, Prin_detalle = Prin_detalle, Prin_fecha = Prin_fecha, Prin_area_id = Prin_area_id, Prin_cliente_id = Prin_cliente_id )

@app.route("/button") 
def Proxima():
    global movreg 
    global sumreg

    if request.method == 'POST':
        if request.form['boton'] == 'atras':
          movreg = movreg - 1
          if movreg == 0:
            movreg = 1
        elif request.form['boton'] == 'adelante':
            movreg = movreg + 1
            if movreg > sumreg:
                movreg = sumreg
        else: 
            print("error")
    elif request.method == 'GET':
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
    Prin_area_id = nickname.area_id
    Prin_cliente_id = nickname.cliente_id
    return render_template("Vista.html", Prin_id = Prin_id, Prin_ticket = Prin_ticket, Prin_detalle = Prin_detalle, Prin_fecha = Prin_fecha, Prin_area_id = Prin_area_id, Prin_cliente_id = Prin_cliente_id )
    


 
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)