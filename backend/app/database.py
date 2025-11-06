from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# ---------------------------------------------------
# CONFIGURACIÓN DE BASE DE DATOS
# ---------------------------------------------------

# Si Render define la variable DATABASE_URL, la usa. Si no, usa SQLite local (útil para pruebas)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./kings_barberia.db")

# Asegurar compatibilidad con PostgreSQL de Render
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

# Sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
