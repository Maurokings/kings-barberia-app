
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from ..models import Barbero
from ..main import engine

router = APIRouter()

@router.get("")
def list_barberos():
    with Session(engine) as session:
        return session.exec(select(Barbero)).all()

@router.post("")
def create_barbero(b: Barbero):
    with Session(engine) as session:
        session.add(b)
        session.commit()
        session.refresh(b)
        return b

@router.put("/{barbero_id}")
def update_barbero(barbero_id: int, b: Barbero):
    with Session(engine) as session:
        existing = session.get(Barbero, barbero_id)
        if not existing:
            raise HTTPException(status_code=404, detail="No encontrado")
        existing.nombre = b.nombre
        existing.porcentaje = b.porcentaje
        existing.activo = b.activo
        session.add(existing)
        session.commit()
        session.refresh(existing)
        return existing
