from fastapi import FastAPI
from app.database import Base, engine
from app.modelos import *
from app import auth
from app.routers import barberos, servicios, cortes, gastos


# Crear la instancia principal de FastAPI
app = FastAPI(title="KINGS Barbería & Peluquería API")

# Crear las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

# Incluir los routers
app.include_router(auth.router)
app.include_router(barberos.router)
app.include_router(servicios.router)
app.include_router(cortes.router)
app.include_router(gastos.router)

@app.get("/")
def root():
    return {"mensaje": "💈 Bienvenido a KINGS Barbería & Peluquería API"}
