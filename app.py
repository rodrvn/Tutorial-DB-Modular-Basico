from flask import Flask
from models import db, User, Startup

app = Flask(__name__)

# configurar la base de datos SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos
db.init_app(app)


@app.route("/agregar")
def hello_world():
    usuario_agregar = User(usuario='Rodri', password='132')
    db.session.add(usuario_agregar)
    db.session.commit()
    return 'se agrego correctamente'


## Breakpoint ##
if __name__ == "__main__":
    app.run (debug=True)
