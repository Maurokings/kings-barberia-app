
from fastapi import APIRouter
from sqlmodel import Session
from ..models import Gasto
from ..main import engine

router = APIRouter()

@router.post("")
def create_gasto(g: Gasto):
    with Session(engine) as session:
        session.add(g)
        session.commit()
        session.refresh(g)
        return g

@router.get("")
def list_gastos():
    with Session(engine) as session:
        with Session(engine) as s:
            return s.exec(__import__('sqlmodel').sqlmodel.select(Gasto)).all()
