from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from bd import *

from bd_simulado import *


#instanciando o app
app = Flask(__name__)

#instanciando o objeto MySQL
mysql = MySQL()
#Ligando o MySQL ao Flask
mysql.init_app(app)

#configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "root"
app.config['MYSQL_DATABASE_DB'] = "escolar"


@app.route("/")
def index ():
    return render_template("index.html")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        login = request.form["login"]
        senha = request.form["senha"]

        #obtendo o cursor para acessar o BD
        cursor = mysql.get_db().cursor()
        idlogin = get_idlogin(cursor, login, senha)


        # verificar se o login está no dicionário
        if idlogin is None:
            return render_template('index.html', erro="Login/Senha inválidos")
        else:
            # obtendo o cursor para acessar o BD
            cursor = mysql.get_db().cursor()
            return render_template('tabela.html', nome=login, historico=get_notas(cursor,idlogin))

    else:
        return render_template("index.html", erro="Método inválido")


@app.route('/detalhe/<id_disc>')
def detalhe(id_disc):
    print(id_disc)
    cursor = mysql.get_db().cursor()
    return render_template("detalhes.html",  detalhes=get_descricao(cursor, id_disc))


@app.route("/infor/<user>/<curso>/<disci>")
def informacoes_disciplina(user,curso,disci):

    return render_template("informacoes_professores.html", disciplina=disci, nome=user, informacoes=get_info_professores(user, disci), curso=curso)


if __name__ == "__main__":
    app.run(debug=True)
