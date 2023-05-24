from flask_sqlalchemy import SQLAlchemy

# Instanciamos SqlAlchemy
db = SQLAlchemy()

#Creamos nuestros modelos(Tablas)
class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)


# Otro Ejemplo
class Startup(db.Model):
    id_startup = db.Column(db.Integer, primary_key=True)
    nombre_empresa = db.Column(db.String)
    descripcion = db.Column(db.String)
    feedback = db.Column(db.String)