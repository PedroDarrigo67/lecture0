from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Inicio"

@app.route("/carga")
def carga():
    return ("Carga.html")

@app.route("/edicion")
def edicion():
    return ("Edicion.html") 

@app.route("/cierre")
def cierre():
    return ("Cierre.html")  

@app.route("/cliente")
def cliente():
    return ("Cierre.html") 


@app.errorhandler(404)
def page_not_found(err):

    return render_template("page_not_found.html"), 404    

@app.errorhandler(403)
def forbidden(err):

    return render_template("unforbidden.html"), 403     

    
if __name__ == "__main__":
    app.run(debug=True) 