from config import *
from model import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar_musicas")
def listar_musicas():
    with db_session:
        # obtém as músicas
        musica = Musica.select() 
        return render_template("listar_musicas.html", musica = musica)

@app.route("/form_adicionar_musica")
def form_adicionar_musica():
    return render_template("form_adicionar_musica.html")

@app.route("/adicionar_musica")
def adicionar_musica():
    # obter os parâmetros
    nome = request.args.get("nome")
    artista = request.args.get("artista")
    duracao = request.args.get("duração")
    genero = request.args.get("gênero")
    # salvar
    with db_session:
        # criar a pessoa
        m = Musica(**request.args)
        # salvar
        commit()
        # encaminhar de volta para a listagem
        return redirect("listar_musicas") 

'''
run:
$ flask run
'''