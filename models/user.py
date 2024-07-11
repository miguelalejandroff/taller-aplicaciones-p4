from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String, nullable=False)
    nombres = db.Column(db.String, nullable=False)
    primer_apellido = db.Column(db.String, nullable=False)
    segundo_apellido = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    direccion = db.Column(db.String)
    comuna_id = db.Column(db.Integer)
    ciudad_id = db.Column(db.Integer)
    centro_id = db.Column(db.Integer)
    fecha_nacimiento = db.Column(db.Date)
    telefono = db.Column(db.String)
    role = db.Column(db.String, nullable=False)