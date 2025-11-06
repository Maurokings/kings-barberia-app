from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import modelos

router = APIRouter(
    prefix="/barberos",
    tags=["Barberos"]
)

# Obtener una sesión de base de datos
def get_db():
    db = modelos.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todos los barberos
@router.get("/")
def obtener_barberos(db: Session = Depends(get_db)):
    barberos = db.query(modelos.Barbero).all()
    return barberos

# Crear un nuevo barbero
@router.post("/")
def crear_barbero(nombre: str, porcentaje_comision: float = 50.0, db: Session = Depends(get_db)):
    nuevo_barbero = modelos.Barbero(nombre=nombre, porcentaje_comision=porcentaje_comision)
    db.add(nuevo_barbero)
    db.commit()
    db.refresh(nuevo_barbero)
    return {"mensaje": "Barbero creado exitosamente", "barbero": nuevo_barbero}

# Actualizar un barbero existente
@router.put("/{barbero_id}")
def actualizar_barbero(barbero_id: int, nombre: str = None, porcentaje_comision: float = None, db: Session = Depends(get_db)):
    barbero = db.query(modelos.Barbero).filter(modelos.Barbero.id == barbero_id).first()
    if not barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado")
    if nombre:
        barbero.nombre = nombre
    if porcentaje_comision is not None:
        barbero.porcentaje_comision = porcentaje_comision
    db.commit()
    db.refresh(barbero)
    return {"mensaje": "Barbero actualizado correctamente", "barbero": barbero}

# Eliminar un barbero
@router.delete("/{barbero_id}")
def eliminar_barbero(barbero_id: int, db: Session = Depends(get_db)):
    barbero = db.query(modelos.Barbero).filter(modelos.Barbero.id == barbero_id).first()
    if not barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado")
    db.delete(barbero)
    db.commit()
    return {"mensaje": "Barbero eliminado correctamente"}
