from sqlalchemy import Column, Integer, String, Text
from database import Base

class Estudiante(Base):
    __tablename__ = "estudiante"

    estudiante_id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String(250), nullable=False)
    carnet = Column(String(10), nullable=False)
    carrera = Column(String(200), nullable=False)
    qr_asistencia = Column(Text, nullable=True)
