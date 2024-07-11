from . import db

class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True)
    ayudantia_id = db.Column(db.Integer, db.ForeignKey('ayudantia.id'), nullable=False)
    fecha = db.Column(db.Date)
    hora_inicio = db.Column(db.Time)
    hora_fin = db.Column(db.Time)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
