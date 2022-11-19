from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required

from models.ModelUser import ModelUser
from models.entities.Usuario import Usuario
 
app = Flask(__name__)

#conexion a base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'modulo_login'
mysql = MySQL(app)
app.secret_key = 'SAADS)#%}!(214/2&%3!3E//RM"PF}DPO##MDWP%#$ODS'

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario(0, request.form['username'], request.form['password'])
        usuarioLogeado = ModelUser.login(mysql, usuario)
        if usuarioLogeado != None:
            if usuarioLogeado.password:
                login_user(usuarioLogeado)
                return redirect(url_for('home'))
            else:
                flash("Contraseña incorrecta")
                return render_template('login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# arrancar la app
if __name__ == '__main__':
    app.run(port = 3000, debug = True)