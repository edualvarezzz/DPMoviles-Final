from fastapi import FastAPI
from database import Base, engine
from routers import auth, estudiantes, actividades, favoritos

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Actividades"
)

# Registramos los routers
app.include_router(auth.router)
app.include_router(estudiantes.router)
app.include_router(actividades.router)
app.include_router(favoritos.router)
