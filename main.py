from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def index():
    escuela = "UTL"
    alumnos = ["Mario", "Pedro", "Luis", "Dario"]

    return render_template("index.html", escuela=escuela, alumnos=alumnos)

@app.route("/hola")
def hola():
    return "<p><h1>Hola desde HOLAA!!!<br/> Mundo</h1></p>"

@app.route("/user/<string:name>")
def user(name):
    return "<h1> Hola +" + name

@app.route("/numero/<int:n>")
def numero(num):
    return "El numero es {}".format(num)

@app.route("/user/<int:id>/<string:name>")
def test(id, name):
    return "ID: {}, Nombre: {}".format(id, name)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma de {} + {} es igual a {}".format(n1, n2, n1 + n2)

@app.route("/default")
@app.route("/default/<string:ab>")
def func1(ab="UTL"):
    return "El valor es " + ab

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

if __name__ == "__main__":
    app.run(debug=True)