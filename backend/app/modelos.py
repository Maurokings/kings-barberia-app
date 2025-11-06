
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

# -------------------------------
# MODELOS (Tablas de la base)
# -------------------------------

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre_usuario = Column(String, unique=True, index=True, nullable=False)
    contraseña = Column(String, nullable=False)
    rol = Column(String, default="admin")  # "admin" o "barbero"


class Barbero(Base):
    __tablename__ = "barberos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    porcentaje = Column(Float, default=50.0)
    contraseña = Column(String, nullable=False)

    cortes = relationship("Corte", back_populates="barbero")


class Servicio(Base):
    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    precio = Column(Float, nullable=False)

    cortes = relationship("Corte", back_populates="servicio")


class Corte(Base):
    __tablename__ = "cortes"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    metodo_pago = Column(String, nullable=False)  # "efectivo" o "transferencia"
    monto = Column(Float, nullable=False)

    barbero_id = Column(Integer, ForeignKey("barberos.id"))
    servicio_id = Column(Integer, ForeignKey("servicios.id"))

    barbero = relationship("Barbero", back_populates="cortes")
    servicio = relationship("Servicio", back_populates="cortes")


class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, nullable=False)
    monto = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)

