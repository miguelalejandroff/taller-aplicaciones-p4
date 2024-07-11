
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .ayudantia import Ayudantia
from .session import Session
from .inscripcionAyudantia import InscripcionAyudantia
from .asistenciaAyudantia import AsistenciaAyudantia
from .feedback import Feedback