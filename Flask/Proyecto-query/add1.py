from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
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
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    nickname = request.args.get("nickname")
    print(nickname)
    user = Principal.query.filter_by(detalle=nickname).first()
    print(user.id)
    return render_template("index.html")


 
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)