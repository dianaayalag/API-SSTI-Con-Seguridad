from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app import db

Base = declarative_base()

class Alumno(db.Model):
    idAlumno = db.Column(db.Integer, primary_key=True)
    usuarioAlumno = db.Column(db.String, unique=True, nullable=False)
    contrasena = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    carrera = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Alumno %r>' % self.usuarioAlumno


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
db.create_all()
