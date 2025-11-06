
from fastapi import FastAPI
from . import modelos, crud
from .routers import auth, barberos, servicios, cortes, gastos
from sqlmodel import SQLModel, create_engine
import os

app = FastAPI(title="KINGS Barberia API")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./kings.db")
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
    crud.create_default_data(engine)

app.include_router(auth.router, prefix="/auth")
app.include_router(barberos.router, prefix="/barberos")
app.include_router(servicios.router, prefix="/servicios")
app.include_router(cortes.router, prefix="/cortes")
app.include_router(gastos.router, prefix="/gastos")
