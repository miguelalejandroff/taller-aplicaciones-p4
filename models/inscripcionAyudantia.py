from . import db

class InscripcionAyudantia(db.Model):
    __tablename__ = 'inscripcion_ayudantia'
    id = db.Column(db.Integer, primary_key=True)
    ayudantia_id = db.Column(db.Integer, db.ForeignKey('ayudantia.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    estado = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
