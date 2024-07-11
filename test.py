import requests
import json

BASE_URL = "http://127.0.0.1:5000"

# Función para probar el registro de usuarios
def test_register_user():
    user_data = {
        "rut": "55555555-5",
        "nombres": "Test",
        "primerApellido": "User",
        "segundoApellido": "Testing",
        "email": "testuser@example.com",
        "direccion": "Test Street 5",
        "comunaID": 5,
        "ciudadID": 5,
        "centroID": 5,
        "fechaNacimiento": "2000-05-05",
        "telefono": "5678901234",
        "role": "estudiante"
    }
    response = requests.post(f"{BASE_URL}/register", json=user_data)
    print(f"Registrar Usuario: {response.status_code} - {response.json()}")

# Función para probar el inicio de sesión
def test_login_user():
    login_data = {
        "rut": "55555555-5",
        "email": "testuser@example.com"
    }
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    print(f"Iniciar Sesión: {response.status_code} - {response.json()}")
    return response.json().get("user")

# Función para probar la creación de ayudantías
def test_create_ayudantia(user_id):
    ayudantia_data = {
        "userID": user_id,
        "estado": "inicial"
    }
    response = requests.post(f"{BASE_URL}/ayudantias", json=ayudantia_data)
    print(f"Crear Ayudantía: {response.status_code} - {response.json()}")
    return response.json().get("id")

# Función para probar la oferta de ayudantías
def test_offer_ayudantia(ayudantia_id):
    response = requests.post(f"{BASE_URL}/ayudantias/{ayudantia_id}/offer")
    try:
        response_data = response.json()
    except ValueError:
        response_data = response.text
    print(f"Ofrecer Ayudantía: {response.status_code} - {response_data}")

# Función para probar la aceptación de ayudantías
def test_accept_ayudantia(ayudantia_id):
    response = requests.post(f"{BASE_URL}/ayudantias/{ayudantia_id}/accept")
    try:
        response_data = response.json()
    except ValueError:
        response_data = response.text
    print(f"Aceptar Ayudantía: {response.status_code} - {response_data}")

# Función para probar la programación de sesiones
def test_schedule_session(ayudantia_id):
    session_data = {
        "fecha": "2024-07-11",
        "horaInicio": "10:00:00",
        "horaFin": "11:00:00"
    }
    response = requests.post(f"{BASE_URL}/ayudantias/{ayudantia_id}/schedule", json=session_data)
    try:
        response_data = response.json()
    except ValueError:
        response_data = response.text
    print(f"Programar Sesión: {response.status_code} - {response_data}")
    return response.json().get("id")

# Función para probar la inscripción en ayudantías
def test_inscripcion_ayudantia(ayudantia_id, user_id):
    inscripcion_data = {
        "ayudantiaID": ayudantia_id,
        "userID": user_id,
        "estado": "inscrito"
    }
    response = requests.post(f"{BASE_URL}/inscripcion_ayudantia", json=inscripcion_data)
    try:
        response_data = response.json()
    except ValueError:
        response_data = response.text
    print(f"Inscripción Ayudantía: {response.status_code} - {response_data}")
    return response.json().get("id")

# Función para probar la asistencia a ayudantías
def test_asistir_ayudantia(inscripcion_id):
    response = requests.post(f"{BASE_URL}/inscripcion_ayudantia/{inscripcion_id}/asistir")
    try:
        response_data = response.json()
    except ValueError:
        response_data = response.text
    print(f"Asistir Ayudantía: {response.status_code} - {response_data}")

# Función para probar la creación de feedback
def test_create_feedback(session_id, user_id):
    feedback_data = {
        "sessionID": session_id,
        "userID": user_id,
        "calificacion": 5.0,
        "comentario": "Muy buena sesión"
    }
    response = requests.post(f"{BASE_URL}/feedback", json=feedback_data)
    try:
        response_data = response.json()
    except ValueError:
        response_data = response.text
    print(f"Crear Feedback: {response.status_code} - {response_data}")

if __name__ == "__main__":
    # Ejecutar todas las pruebas
    test_register_user()
    user_id = test_login_user()
    ayudantia_id = test_create_ayudantia(user_id)
    test_offer_ayudantia(ayudantia_id)
    test_accept_ayudantia(ayudantia_id)
    session_id = test_schedule_session(ayudantia_id)
    inscripcion_id = test_inscripcion_ayudantia(ayudantia_id, user_id)
    test_asistir_ayudantia(inscripcion_id)
    test_create_feedback(session_id, user_id)
