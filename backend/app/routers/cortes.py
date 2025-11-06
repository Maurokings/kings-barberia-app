from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.modelos import Corte, Barbero, Servicio
from datetime import datetime

router = APIRouter(prefix="/cortes", tags=["Cortes"])

# Dependencia para obtener la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Registrar un corte (servicio realizado)
@router.post("/")
def registrar_corte(
    barbero_id: int,
    servicio_id: int,
    metodo_pago: str,
    monto: float,
    db: Session = Depends(get_db)
):
    if metodo_pago.lower() not in ["efectivo", "transferencia"]:
        raise HTTPException(status_code=400, detail="Método de pago inválido. Use 'efectivo' o 'transferencia'.")

    barbero = db.query(Barbero).filter(Barbero.id == barbero_id).first()
    servicio = db.query(Servicio).filter(Servicio.id == servicio_id).first()

    if not barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado.")
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado.")

    nuevo_corte = Corte(
        barbero_id=barbero.id,
        servicio_id=servicio.id,
        metodo_pago=metodo_pago.lower(),
        monto=monto,
        fecha=datetime.utcnow()
    )

    db.add(nuevo_corte)
    db.commit()
    db.refresh(nuevo_corte)

    return {
        "mensaje": f"✅ Corte registrado para {barbero.nombre} ({servicio.nombre})",
        "metodo_pago": metodo_pago,
        "monto": monto,
        "fecha": nuevo_corte.fecha
    }

# ✅ Listar todos los cortes
@router.get("/")
def listar_cortes(db: Session = Depends(get_db)):
    cortes = db.query(Corte).all()
    return cortes

