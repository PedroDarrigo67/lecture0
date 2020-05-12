from flask import Flask

app = Flask(__name__) # name toma nombre del archivo py

@app.route("/")
def index():
    print(__name__)
    return "Hello Pedro"

@app.route("/hola") #normalmente la funcion se llama como la ruta
def hola():
    return "hola Yo"
    
@app.route("/user/<string:user>") #manejo de variables en barra de direcciones
def user(user):
    return "Hola " + user

#@app.route("/numero/<int:n>") #manejo entero
#def numero(n):
#   return "Numero: {}".format{n}

    

if __name__ == "__main__":
    app.run(debug=True)   #modo debug actualiza los cambios, aca se carga puertos e ip