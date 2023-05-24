from models import db, User, Startup
from flask import Flask

app = Flask('app')

# configurar la base de datos SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Crear base de datoos
with app.app_context():
    db.create_all()