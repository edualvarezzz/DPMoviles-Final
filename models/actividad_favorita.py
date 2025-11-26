from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class ActividadFavorita(Base):
    __tablename__ = "actividad_favorita"

    actividad_favorita_id = Column(Integer, primary_key=True, index=True)
    estudiante_id = Column(Integer, ForeignKey("estudiante.estudiante_id"))
    conferencia_id = Column(Integer, ForeignKey("actividad.conferencia_id"))
