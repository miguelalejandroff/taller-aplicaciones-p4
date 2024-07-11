-- Crear tabla de usuarios
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rut VARCHAR NOT NULL,
    nombres VARCHAR NOT NULL,
    primerApellido VARCHAR NOT NULL,
    segundoApellido VARCHAR,
    email VARCHAR NOT NULL UNIQUE,
    direccion VARCHAR,
    comunaID INTEGER,
    ciudadID INTEGER,
    centroID INTEGER,
    fechaNacimiento DATE,
    telefono VARCHAR,
    FOREIGN KEY (comunaID) REFERENCES comunas(id),
    FOREIGN KEY (ciudadID) REFERENCES ciudades(id),
    FOREIGN KEY (centroID) REFERENCES centros(id)
);

-- Crear tabla de ayudantías
CREATE TABLE ayudantia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER NOT NULL,
    estado VARCHAR,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (userID) REFERENCES users(id)
);

-- Crear tabla de sesiones
CREATE TABLE sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ayudantiaID INTEGER NOT NULL,
    fecha DATE,
    horaInicio TIME,
    horaFin TIME,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ayudantiaID) REFERENCES ayudantia(id)
);

-- Crear tabla de inscripción a ayudantías
CREATE TABLE inscripcion_ayudantia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ayudantiaID INTEGER NOT NULL,
    userID INTEGER NOT NULL,
    estado VARCHAR,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ayudantiaID) REFERENCES ayudantia(id),
    FOREIGN KEY (userID) REFERENCES users(id)
);

-- Crear tabla de asistencia a ayudantías
CREATE TABLE asistencia_ayudantia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    inscripcionID INTEGER NOT NULL,
    estado VARCHAR,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (inscripcionID) REFERENCES inscripcion_ayudantia(id)
);

-- Crear tabla de feedback
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sessionID INTEGER NOT NULL,
    userID INTEGER NOT NULL,
    calificacion FLOAT,
    comentario TEXT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sessionID) REFERENCES sessions(id),
    FOREIGN KEY (userID) REFERENCES users(id)
);
