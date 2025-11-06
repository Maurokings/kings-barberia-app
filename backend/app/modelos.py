
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password_hash: str
    nombre: Optional[str] = None
    rol: str = "admin"  # admin | barbero | secretaria

class Barbero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    porcentaje: float = 50.0
    activo: bool = True

class Servicio(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    precio_sugerido: float = 0.0
    activo: bool = True

class Corte(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: datetime = Field(default_factory=datetime.utcnow)
    barbero_id: Optional[int] = None
    servicio_id: Optional[int] = None
    monto: float = 0.0
    metodo_pago: str = "efectivo"  # efectivo | transferencia
    comision_barbero: float = 0.0
    ganancia_barberia: float = 0.0

class Gasto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: datetime = Field(default_factory=datetime.utcnow)
    descripcion: Optional[str] = None
    monto: float = 0.0
    metodo_pago: str = "efectivo"
