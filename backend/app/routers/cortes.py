
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import modelos
from datetime import datetime

router = APIRouter(
    prefix="/cortes",
    tags=["Cortes"]
)

# Obtener todos los cortes registrados
@router.get("/")
def obtener_cortes(db: Session = Depends(get_db)):
    return db.query(modelos.Corte).order_by(modelos.Corte.fecha.desc()).all()

# Registrar un nuevo corte
@router.post("/")
def registrar_corte(
    barbero_id: int,
    servicio_id: int,
    metodo_pago: str,
    monto: float,
    db: Session = Depends(get_db)
):
    barbero = db.query(modelos.Barbero).filter(modelos.Barbero.id == barbero_id).first()
    servicio = db.query(modelos.Servicio).filter(modelos.Servicio.id == servicio_id).first()

    if not barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado.")
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado.")
    if metodo_pago not in ["efectivo", "transferencia"]:
        raise HTTPException(status_code=400, detail="Método de pago inválido. Use 'efectivo' o 'transferencia'.")

    nuevo_corte = modelos.Corte(
        barbero_id=barbero_id,
        servicio_id=servicio_id,
        metodo_pago=metodo_pago,
        monto=monto,
        fecha=datetime.utcnow()
    )

    db.add(nuevo_corte)
    db.commit()
    db.refresh(nuevo_corte)

    return {
        "mensaje": "Corte registrado correctamente",
        "corte": {
            "id": nuevo_corte.id,
            "barbero": barbero.nombre,
            "servicio": servicio.nombre,
            "monto": nuevo_corte.monto,
            "metodo_pago": nuevo_corte.metodo_pago,
            "fecha": nuevo_corte.fecha
        }
    }

# Eliminar un corte
@router.delete("/{corte_id}")
def eliminar_corte(corte_id: int, db: Session = Depends(get_db)):
    corte = db.query(modelos.Corte).filter(modelos.Corte.id == corte_id).first()
    if not corte:
        raise HTTPException(status_code=404, detail="Corte no encontrado.")
    db.delete(corte)
    db.commit()
    return {"mensaje": "Corte eliminado correctamente"}
