from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
#request es para ambos metodos
#post envia la informacion mas privava, get lo envia po url

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)





class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)




@app.route("/")
def index():
    return render_template("index.html")




@app.route("/search")
def search():
    nickname = request.args.get("nickname")
    print(nickname)
    user = Users.query.filter_by(username=nickname).first()
    
    print(user.password)
    if user:
        return render_template("login.html")
    return "Usuario no existe"







@app.route("/signup", methods=["GET", "POST"]) #ruta por defecto son metodo get
def signup(): #funcion, le ponemos que sean ambos metodos
    if request.method == "POST":
        hashed_pw = generate_password_hash(request.form["password"], method="sha256")
        #cifrado de contrasena
        new_user = Users(username=request.form["username"], password=hashed_pw)
        #Objeto user, y le cargamos las variables
        db.session.add(new_user) #adherimos a base de datos
        db.session.commit() #grabamos
        return "Registrado con exito"
    return render_template("signup.html")





@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            return "Ya esta ingresado"
        return "Su credencial no es valida"
    return render_template("login.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)