from flask import Flask, request, jsonify
from models import db, User, Ayudantia, Session, InscripcionAyudantia, AsistenciaAyudantia, Feedback
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    new_user = User(
        rut=data['rut'],
        nombres=data['nombres'],
        primer_apellido=data['primerApellido'],
        segundo_apellido=data.get('segundoApellido'),
        email=data['email'],
        direccion=data.get('direccion'),
        comuna_id=data.get('comunaID'),
        ciudad_id=data.get('ciudadID'),
        centro_id=data.get('centroID'),
        fecha_nacimiento=datetime.strptime(data['fechaNacimiento'], '%Y-%m-%d').date(),
        telefono=data.get('telefono'),
        role=data.get('role')  # Agregado campo de rol
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"mensaje": f"Usuario {new_user.nombres} {new_user.primer_apellido} registrado exitosamente"}), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.rut == data['rut']:
        return jsonify({"mensaje": f"Inicio de sesión exitoso para el usuario {user.nombres}", "user": user.id, "role": user.role}), 200
    return jsonify({"mensaje": "Credenciales inválidas"}), 401

@app.route('/ayudantias', methods=['POST'])
def create_ayudantia():
    data = request.get_json()
    new_ayudantia = Ayudantia(
        user_id=data['userID'],
        estado=data.get('estado')
    )
    db.session.add(new_ayudantia)
    db.session.commit()
    return jsonify({"mensaje": f"Ayudantía creada exitosamente con ID {new_ayudantia.id} para el usuario {new_ayudantia.user_id}", "id": new_ayudantia.id}), 201

@app.route('/ayudantias/<int:ayudantia_id>/offer', methods=['POST'])
def offer_ayudantia(ayudantia_id):
    ayudantia = Ayudantia.query.get(ayudantia_id)
    if ayudantia:
        ayudantia.estado = 'ofrecida'
        db.session.commit()
        return jsonify({"mensaje": f"Ayudantía con ID {ayudantia.id} ofrecida exitosamente"}), 200
    return jsonify({"mensaje": "Ayudantía no encontrada"}), 404

@app.route('/ayudantias/<int:ayudantia_id>/accept', methods=['POST'])
def accept_ayudantia(ayudantia_id):
    ayudantia = Ayudantia.query.get(ayudantia_id)
    if ayudantia:
        ayudantia.estado = 'aceptada'
        db.session.commit()
        return jsonify({"mensaje": f"Ayudantía con ID {ayudantia.id} aceptada exitosamente"}), 200
    return jsonify({"mensaje": "Ayudantía no encontrada"}), 404

@app.route('/ayudantias/<int:ayudantia_id>/schedule', methods=['POST'])
def schedule_session(ayudantia_id):
    data = request.get_json()
    new_session = Session(
        ayudantia_id=ayudantia_id,
        fecha=datetime.strptime(data['fecha'], '%Y-%m-%d').date(),
        hora_inicio=datetime.strptime(data['horaInicio'], '%H:%M:%S').time(),
        hora_fin=datetime.strptime(data['horaFin'], '%H:%M:%S').time()
    )
    db.session.add(new_session)
    db.session.commit()
    return jsonify({"mensaje": f"Sesión agendada exitosamente para la ayudantía con ID {ayudantia_id}", "id": new_session.id}), 201

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

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        user_data = {
            'id': user.id,
            'rut': user.rut,
            'nombres': user.nombres,
            'primer_apellido': user.primer_apellido,
            'segundo_apellido': user.segundo_apellido,
            'email': user.email,
            'direccion': user.direccion,
            'comuna_id': user.comuna_id,
            'ciudad_id': user.ciudad_id,
            'centro_id': user.centro_id,
            'fecha_nacimiento': user.fecha_nacimiento,
            'telefono': user.telefono,
            'role': user.role
        }
        result.append(user_data)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
