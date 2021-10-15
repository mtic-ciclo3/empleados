from flask import Flask, render_template, request, flash
#from werkzeug.utils import redirect
#import utils

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('retroalimentacion.html')

@app.route("/retroalimentacion", methods = ["POST"])
def retroalimentacion():
    try:
        if  request.method == "POST":
            username = request.form['username']
            password = request.form['password']

            if not utils.isUsernameValid(username):
                error = "El usuario debe ser alfanumerico o incluir solo '.','_','-'"
                flash(error)
                return render_template('retroalimentacion.html')

            if not utils.isPasswordValid(password):
                error = 'La contraseña debe contener al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash(error)
                return render_template('retroalimentacion.html')

    except:
        return render_template("retroalimentacion.html")

@app.route('/creausuario')
def creausuario():
    return render_template("crea_usuario.html")