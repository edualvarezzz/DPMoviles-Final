from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.actividad_favorita import ActividadFavorita
from models.actividad import Actividad

router = APIRouter(prefix="/favoritos", tags=["Favoritos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{id_estudiante}/{id_actividad}")
def marcar_favorito(id_estudiante: int, id_actividad: int, db: Session = Depends(get_db)):
    existe = db.query(ActividadFavorita).filter(
        ActividadFavorita.estudiante_id == id_estudiante,
        ActividadFavorita.conferencia_id == id_actividad
    ).first()

    if existe:
        raise HTTPException(status_code=400, detail="Ya es favorito")

    fav = ActividadFavorita(
        estudiante_id=id_estudiante,
        conferencia_id=id_actividad
    )
    db.add(fav)
    db.commit()

    return {"mensaje": "Actividad marcada como favorita"}


@router.delete("/{actividad_favorita_id}")
def eliminar_favorito(actividad_favorita_id: int, db: Session = Depends(get_db)):
    registro = db.query(ActividadFavorita).filter(
        ActividadFavorita.actividad_favorita_id == actividad_favorita_id
    ).first()

    if not registro:
        raise HTTPException(status_code=404, detail="Registro de favorito no encontrado")

    db.delete(registro)
    db.commit()

    return {"mensaje": "Favorito eliminado correctamente"}




@router.get("/estudiante/{id_estudiante}")
def listar_favoritos(id_estudiante: int, db: Session = Depends(get_db)):
    favoritos = db.query(ActividadFavorita).filter(
        ActividadFavorita.estudiante_id == id_estudiante
    ).all()

    resultado = []

    for fav in favoritos:
        actividad = db.query(Actividad).filter(
            Actividad.conferencia_id == fav.conferencia_id
        ).first()

        if actividad:
            resultado.append({
                "actividad_favorita_id": fav.actividad_favorita_id,
                "conferencia_id": actividad.conferencia_id,
                "titulo": actividad.titulo,
                "encargado": actividad.encargado,
                "hora_inicio": str(actividad.hora_inicio),
                "hora_fin": str(actividad.hora_fin),
                "salon": actividad.salon,
                "descripcion": actividad.descripcion
            })

    return resultado