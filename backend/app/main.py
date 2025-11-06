
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import modelos, crud
from app.database import engine, Base
from app.routers import auth, barberos, servicios, cortes, gastos

# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kings Barbería & Peluquería API")

# Configurar CORS para permitir peticiones desde el frontend
origins = ["*"]  # Luego podés poner tu dominio exacto

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers
app.include_router(auth.router)
app.include_router(barberos.router)
app.include_router(servicios.router)
app.include_router(cortes.router)
app.include_router(gastos.router)

@app.get("/")
def root():
    return {"mensaje": "API de Kings Barbería funcionando correctamente 😎"}
