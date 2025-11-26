from sqlalchemy import Column, Integer, String, Time
from database import Base

class Actividad(Base):
    __tablename__ = "actividad"

    conferencia_id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    encargado = Column(String(200), nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)
    salon = Column(String(20), nullable=False)
    descripcion = Column(String(200), nullable=False)
