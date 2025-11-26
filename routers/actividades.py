from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.actividad import Actividad

router = APIRouter(prefix="/actividades", tags=["Actividades"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar_actividades(db: Session = Depends(get_db)):
    return db.query(Actividad).all()
