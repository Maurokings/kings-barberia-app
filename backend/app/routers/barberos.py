from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import modelos

router = APIRouter(
    prefix="/barberos",
    tags=["Barberos"]
)

# Obtener todos los barberos
@router.get("/")
def obtener_barberos(db: Session = Depends(get_db)):
    return db.query(modelos.Barbero).all()

# Crear un nuevo barbero
@router.post("/")
def crear_barbero(nombre: str, porcentaje: float = 50.0, contraseña: str = "1234", db: Session = Depends(get_db)):
    existente = db.query(modelos.Barbero).filter(modelos.Barbero.nombre == nombre).first()
    if existente:
        raise HTTPException(status_code=400, detail="El barbero ya existe.")
    nuevo = modelos.Barbero(nombre=nombre, porcentaje=porcentaje, contraseña=contraseña)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Barbero creado exitosamente", "barbero": nuevo}

# Actualizar barbero
@router.put("/{barbero_id}")
def actualizar_barbero(barbero_id: int, nombre: str = None, porcentaje: float = None, db: Session = Depends(get_db)):
    barbero = db.query(modelos.Barbero).filter(modelos.Barbero.id == barbero_id).first()
    if not barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado.")
    if nombre:
        barbero.nombre = nombre
    if porcentaje is not None:
        barbero.porcentaje = porcentaje
    db.commit()
    db.refresh(barbero)
    return {"mensaje": "Barbero actualizado", "barbero": barbero}

# Eliminar barbero
@router.delete("/{barbero_id}")
def eliminar_barbero(barbero_id: int, db: Session = Depends(get_db)):
    barbero = db.query(modelos.Barbero).filter(modelos.Barbero.id == barbero_id).first()
    if not barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado.")
    db.delete(barbero)
    db.commit()
    return {"mensaje": "Barbero eliminado correctamente"}
