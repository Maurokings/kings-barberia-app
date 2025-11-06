
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from ..models import Servicio
from ..main import engine

router = APIRouter()

@router.get("")
def list_servicios():
    with Session(engine) as session:
        return session.exec(select(Servicio)).all()

@router.post("")
def create_servicio(s: Servicio):
    with Session(engine) as session:
        session.add(s)
        session.commit()
        session.refresh(s)
        return s

@router.put("/{servicio_id}")
def update_servicio(servicio_id: int, s: Servicio):
    with Session(engine) as session:
        existing = session.get(Servicio, servicio_id)
        if not existing:
            raise HTTPException(status_code=404, detail="No encontrado")
        existing.nombre = s.nombre
        existing.precio_sugerido = s.precio_sugerido
        existing.activo = s.activo
        session.add(existing)
        session.commit()
        session.refresh(existing)
        return existing
