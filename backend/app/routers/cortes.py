
from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from ..models import Corte, Barbero
from ..main import engine

router = APIRouter()

@router.post("")
def create_corte(c: Corte):
    with Session(engine) as session:
        barbero = session.get(Barbero, c.barbero_id)
        if not barbero:
            raise HTTPException(status_code=404, detail="Barbero no encontrado")
        # calculate commission
        c.comision_barbero = round(c.monto * (barbero.porcentaje/100), 2)
        c.ganancia_barberia = round(c.monto - c.comision_barbero, 2)
        session.add(c)
        session.commit()
        session.refresh(c)
        return c

@router.get("")
def list_cortes():
    with Session(engine) as session:
        return session.exec(select(Corte)).all()
