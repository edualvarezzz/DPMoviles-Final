from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from utils.hash import verify_password
from utils.jwt_handler import create_access_token
from models.estudiante import Estudiante
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginData(BaseModel):
    usuario: str
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(data: LoginData, db: Session = Depends(get_db)):
    user = db.query(Estudiante).filter(Estudiante.usuario == data.usuario).first()

    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    token = create_access_token({"id": user.estudiante_id})

    return {
        "access_token": token,
        "token_type": "bearer",
        "estudiante": {
            "estudiante_id": user.estudiante_id,
            "nombre_completo": user.nombre_completo
        }
    }

