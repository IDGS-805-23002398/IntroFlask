#
from flask import Flask, render_template, request
from flask import flash #Mandar datos desde la ruta hasta la vista
from flask_wtf.csrf import CSRFProtect # Proteccion contra la usurpacion de identidad

import forms


app = Flask(__name__)
app.secret_key='Clave secreta'
csrf = CSRFProtect()

@app.route("/")
def index():
    titulo = "IDGS-805-Flask"
    lista = ["Huan", "Mario", "Pedro"]
    return render_template("index.html", titulo=titulo, lista=lista)


@app.route("/usuarios", methods=['GET','POST'])
def usuarios(): 
    mat=0
    nom=''
    apa=''
    ama=''
    email=''
    usuarios_class= forms.UserForm(request.form) # Se vincula la clase con la vista
    if request.method == 'POST' and usuarios_class.validate():
        mat=usuarios_class.matricula.data
        nom = usuarios_class.nombre.data
        apa = usuarios_class.aPaterno.data
        ama = usuarios_class.aMaterno.data
        email = usuarios_class.correo.data
        
        mensaje = "Bienvenido {}".format(nom)
        flash(mensaje)
        
    return render_template("usuarios.html", 
                           form=usuarios_class, # Asi se pasan los objetos / clases
                           mat = mat,
                           nom=nom,
                           apa=apa,
                           ama=ama,
                           email=email
                           )

# @app.route("/usuarios")
# def form():  # El nombre que quieras
#     return render_template("formularios.html")


@app.route("/reportes")
def report():  # El nombre que quieras
    return render_template("reportes.html")


@app.route("/hola")
def hola():  # El nombre que quieras
    return "Hola desde /hola"


@app.route("/user/<string:user>")  # Rutas con parametros
def user(user):
    return f"Hola {user}"  # Se usa la f para dar formato a la variable


@app.route("/numero/<int:n>")
def number(n):
    return (
        f"Este es el numero: {n}"  # Se puede usar el .format(variable) en vez de la f
    )


@app.route("/float/<float:num1>/<float:num2>")
def decimal(num1, num2):
    return f"Este es el numero: {num1 + num2}"


@app.route("/user/<int:id>/<string:username>")
def credenciales(id, username):
    return f"ID: {id} nombre: {username}"


@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>Hola {param}</h1>"


@app.route("/operas")
def operas():
    return """
<form>
<label for="name"> Name: </label>
<input type="text" id="name" name="name" required>
<label for="name"> Apaterno: </label>
<input type="text" id="name" name="name" required>
</form>

        """

@app.route("/operasBas", methods =["GET","POST"])
def operas1():
    n1=0
    n2=0
    res =0
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        res = float(n1)+float(n2)
    return render_template("operasBas.html",n1=n1,n2=n2,res=res)

@app.route("/cinepolis", methods=["GET","POST"])
def cinepolis():
    nom=""
    cantiCom = 0
    isCineco=""
    cantiBol=0
    Total =0
    alert = ""
    cinepolis_class = forms.CinepolisForm(request.form)
    if request.method == "POST" and cinepolis_class.validate():
        nom = cinepolis_class.nombre.data
        cantiCom = cinepolis_class.compradores.data
        isCineco = cinepolis_class.cineco.data
        cantiBol = cinepolis_class.boletos.data
        limit = cantiCom * 7
        if cantiBol <= limit:
            Total = cantiBol*12
            if cantiBol == 3 or cantiBol == 4 or cantiBol == 5:
                Total *= 0.90
            if cantiBol > 5:
                Total *= 0.85
            if isCineco == "si":
                Total *= 0.90
        else:
            Total = 0
            alert = "Solo se permiten 7 boletos por comprador. La cantidad ingresada es incorrecta."
            flash(alert)
    return render_template("cinepolis.html",form=cinepolis_class ,nom = nom, cantiCom= cantiCom,isCineco=isCineco,cantiBol=cantiBol, Total=Total)

@app.route("/alumnos")
def alumnos():
        return render_template("alumnos.html")
    
@app.route("/distancia", methods =["GET","POST"])
def distancia():
    x1 = 0
    y1=0
    x2 = 0
    y2=0
    res = 0
    if request.method == "POST":
        x1 = request.form.get("x1")
        y1= request.form.get("y1")
        x2 = request.form.get("x2")
        y2= request.form.get("y2")
        res = (pow(float(x2)- float(x1),2) + pow(float(y2)- float(y1),2))** (0.5) 
    return render_template("distancia.html",x1=x1,y1=y1,x2=x2,y2=y2,res=res)

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    opera = request.form.get("opera")
    if opera == "+":
        return f"La suma es: {float(n1) + float(n2) }"
    if opera == "-":
        return f"La resta es: {float(n1) - float(n2) }"
    if opera == "*":
        return f"La multiplicacion es: {float(n1) * float(n2) }"
    if opera == "/":
        return f"La division es: {float(n1) / float(n2)}"


if __name__ == "__main__":
    csrf.init_app(app) # Valida a cada una de las aplicaciones que hay aqui
    app.run(debug=True)  # Para que se actualicen los cambios se pone en true
