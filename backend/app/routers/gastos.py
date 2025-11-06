from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.database import SessionLocal
from app.modelos import Corte, Barbero, Gasto

router = APIRouter(prefix="/resumen", tags=["Resumenes"])

# Dependencia para obtener la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Resumen diario
@router.get("/diario")
def resumen_diario(db: Session = Depends(get_db)):
    hoy = datetime.utcnow().date()
    inicio = datetime(hoy.year, hoy.month, hoy.day)
    fin = inicio + timedelta(days=1)

    cortes = db.query(Corte).filter(Corte.fecha >= inicio, Corte.fecha < fin).all()
    if not cortes:
        return {"mensaje": "No hay cortes registrados para hoy."}

    efectivo = sum(c.monto for c in cortes if c.metodo_pago == "efectivo")
    transferencia = sum(c.monto for c in cortes if c.metodo_pago == "transferencia")
    total = efectivo + transferencia

    resumen_barberos = []
    for barbero in db.query(Barbero).all():
        cortes_barbero = [c for c in cortes if c.barbero_id == barbero.id]
        total_barbero = sum(c.monto for c in cortes_barbero)
        comision = total_barbero * (barbero.porcentaje / 100)
        resumen_barberos.append({
            "barbero": barbero.nombre,
            "porcentaje": barbero.porcentaje,
            "total_cortes": len(cortes_barbero),
            "total_recaudado": total_barbero,
            "comision_barbero": comision,
            "ganancia_barberia": total_barbero - comision
        })

    return {
        "fecha": str(hoy),
        "efectivo": efectivo,
        "transferencia": transferencia,
        "total_dia": total,
        "resumen_por_barbero": resumen_barberos
    }

# ✅ Resumen semanal
@router.get("/semanal")
def resumen_semanal(db: Session = Depends(get_db)):
    hoy = datetime.utcnow().date()
    inicio_semana = hoy - timedelta(days=hoy.weekday())  # Lunes
    inicio = datetime(inicio_semana.year, inicio_semana.month, inicio_semana.day)
    fin = inicio + timedelta(days=7)

    cortes = db.query(Corte).filter(Corte.fecha >= inicio, Corte.fecha < fin).all()
    if not cortes:
        return {"mensaje": "No hay cortes registrados esta semana."}

    efectivo = sum(c.monto for c in cortes if c.metodo_pago == "efectivo")
    transferencia = sum(c.monto for c in cortes if c.metodo_pago == "transferencia")
    total = efectivo + transferencia

    resumen_barberos = []
    for barbero in db.query(Barbero).all():
        cortes_barbero = [c for c in cortes if c.barbero_id == barbero.id]
        total_barbero = sum(c.monto for c in cortes_barbero)
        comision = total_barbero * (barbero.porcentaje / 100)
        resumen_barberos.append({
            "barbero": barbero.nombre,
            "porcentaje": barbero.porcentaje,
            "total_cortes": len(cortes_barbero),
            "total_recaudado": total_barbero,
            "comision_barbero": comision,
            "ganancia_barberia": total_barbero - comision
        })

    return {
        "desde": str(inicio.date()),
        "hasta": str((fin - timedelta(days=1)).date()),
        "efectivo": efectivo,
        "transferencia": transferencia,
        "total_semana": total,
        "resumen_por_barbero": resumen_barberos
    }

