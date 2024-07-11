from flask import Flask, request, jsonify
from models import db, User, Ayudantia, Session, InscripcionAyudantia, AsistenciaAyudantia, Feedback
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/inscripcion_ayudantia', methods=['POST'])
def create_inscripcion_ayudantia():
    data = request.get_json()
    new_inscripcion = InscripcionAyudantia(
        ayudantia_id=data['ayudantiaID'],
        user_id=data['userID'],
        estado=data['estado']
    )
    db.session.add(new_inscripcion)
    db.session.commit()
    return jsonify({"mensaje": f"Inscripción en la ayudantía con ID {new_inscripcion.ayudantia_id} creada exitosamente", "id": new_inscripcion.id}), 201

@app.route('/inscripcion_ayudantia/<int:inscripcion_id>/asistir', methods=['POST'])
def asistir_ayudantia(inscripcion_id):
    inscripcion = InscripcionAyudantia.query.get(inscripcion_id)
    if inscripcion:
        nueva_asistencia = AsistenciaAyudantia(
            inscripcion_id=inscripcion_id,
            estado='asistida'
        )
        db.session.add(nueva_asistencia)
        db.session.commit()
        return jsonify({"mensaje": f"Asistencia registrada exitosamente para la inscripción con ID {inscripcion_id}"}), 201
    return jsonify({"mensaje": "Inscripción de ayudantía no encontrada"}), 404

@app.route('/feedback', methods=['POST'])
def create_feedback():
    data = request.get_json()
    new_feedback = Feedback(
        session_id=data['sessionID'],
        user_id=data['userID'],
        calificacion=data.get('calificacion'),
        comentario=data.get('comentario')
    )
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify({"mensaje": f"Feedback creado exitosamente para la sesión con ID {new_feedback.session_id}"}), 201


@app.route('/ayudantias', methods=['GET'])
def get_ayudantias():
    ayudantias = Ayudantia.query.all()
    result = []
    for ayudantia in ayudantias:
        ayudantia_data = {
            'id': ayudantia.id,
            'user_id': ayudantia.user_id,
            'estado': ayudantia.estado,
            'created_at': ayudantia.created_at,
            'updated_at': ayudantia.updated_at
        }
        result.append(ayudantia_data)
    return jsonify(result), 200

@app.route('/asistencia_ayudantia', methods=['GET'])
def get_asistencia_ayudantia():
    asistencias = AsistenciaAyudantia.query.all()
    result = []
    for asistencia in asistencias:
        asistencia_data = {
            'id': asistencia.id,
            'inscripcion_id': asistencia.inscripcion_id,
            'estado': asistencia.estado,
            'created_at': asistencia.created_at,
            'updated_at': asistencia.updated_at
        }
        result.append(asistencia_data)
    return jsonify(result), 200

@app.route('/feedback', methods=['GET'])
def get_feedback():
    feedbacks = Feedback.query.all()
    result = []
    for feedback in feedbacks:
        feedback_data = {
            'id': feedback.id,
            'session_id': feedback.session_id,
            'user_id': feedback.user_id,
            'calificacion': feedback.calificacion,
            'comentario': feedback.comentario,
            'created_at': feedback.created_at,
            'updated_at': feedback.updated_at
        }
        result.append(feedback_data)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
