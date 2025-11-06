
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import modelos
from datetime import datetime

router = APIRouter(
    prefix="/gastos",
    tags=["Gastos"]
)

# Obtener todos los gastos
@router.get("/")
def obtener_gastos(db: Session = Depends(get_db)):
    return db.query(modelos.Gasto).order_by(modelos.Gasto.fecha.desc()).all()

# Registrar un nuevo gasto
@router.post("/")
def registrar_gasto(descripcion: str, monto: float, db: Session = Depends(get_db)):
    if monto <= 0:
        raise HTTPException(status_code=400, detail="El monto debe ser mayor a 0.")
    nuevo_gasto = modelos.Gasto(descripcion=descripcion, monto=monto, fecha=datetime.utcnow())
    db.add(nuevo_gasto)
    db.commit()
    db.refresh(nuevo_gasto)
    return {"mensaje": "Gasto registrado correctamente", "gasto": nuevo_gasto}

# Eliminar un gasto
@router.delete("/{gasto_id}")
def eliminar_gasto(gasto_id: int, db: Session = Depends(get_db)):
    gasto = db.query(modelos.Gasto).filter(modelos.Gasto.id == gasto_id).first()
    if not gasto:
        raise HTTPException(status_code=404, detail="Gasto no encontrado.")
    db.delete(gasto)
    db.commit()
    return {"mensaje": "Gasto eliminado correctamente"}
