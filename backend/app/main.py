from fastapi import FastAPI
from app.database import Base, engine
from app.modelos import *
from app import auth
from app.routers import barberos, servicios, cortes, gastos


# Crear la instancia principal de FastAPI
app = FastAPI(title="KINGS Barbería & Peluquería API")
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://kings-barberia-app1.vercel.app",  # tu frontend
        "https://kings-barberia-app.vercel.app",   # por las dudas del alias
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
