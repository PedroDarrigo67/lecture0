from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database1.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    nro_ticket = db.Column (db.Integer, unique=True, nullable=False )
    fecha = db.Column (db.String(8), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)


@app.route("/")
def index():
    return "Home!"

@app.route("/insert/person")
def insert_default():
    new_post = Address(email) 
    db.session.add(new_post) 
    db.session.commit() 
    return "tabla cargada"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)