from pydantic import BaseModel, EmailStr
from typing import Optional

class EstudianteCreate(BaseModel):
	nombre: str
	apellido: Optional[str] = None
	correo: Optional[EmailStr] = None

class EstudianteOut(BaseModel):
	estudiante_id: int
	nombre: str
	apellido: Optional[str] = None
	correo: Optional[EmailStr] = None
	class Config:
		orm_mode = True