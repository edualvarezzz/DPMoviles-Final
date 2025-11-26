from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.estudiante import Estudiante
from pydantic import BaseModel
from utils.qr_generator import generar_qr

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])

class EstudianteData(BaseModel):
    nombre_completo: str
    carnet: str
    carrera: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def crear_estudiante(data: EstudianteData, db: Session = Depends(get_db)):

    qr_text = f"{data.nombre_completo} | {data.carnet} | {data.carrera}"
    qr_path = generar_qr(qr_text)

    nuevo = Estudiante(
        nombre_completo=data.nombre_completo,
        carnet=data.carnet,
        carrera=data.carrera,
        qr_asistencia=qr_path
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo


@router.put("/{id}")
def actualizar_estudiante(id: int, data: EstudianteData, db: Session = Depends(get_db)):
    estudiante = db.query(Estudiante).filter(Estudiante.estudiante_id == id).first()

    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    # generar nuevo QR
    qr_text = f"{data.nombre_completo} | {data.carnet} | {data.carrera}"
    qr_path = generar_qr(qr_text)

    estudiante.nombre_completo = data.nombre_completo
    estudiante.carnet = data.carnet
    estudiante.carrera = data.carrera
    estudiante.qr_asistencia = qr_path

    db.commit()
    db.refresh(estudiante)

    return {
        "id": estudiante.estudiante_id,
        "nombre_completo": estudiante.nombre_completo,
        "carnet": estudiante.carnet,
        "carrera": estudiante.carrera,
        "qr_asistencia": estudiante.qr_asistencia
    }

