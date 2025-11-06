
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import modelos

router = APIRouter(
    prefix="/servicios",
    tags=["Servicios"]
)

# Obtener todos los servicios
@router.get("/")
def obtener_servicios(db: Session = Depends(get_db)):
    return db.query(modelos.Servicio).all()

# Crear un servicio nuevo
@router.post("/")
def crear_servicio(nombre: str, precio: float, db: Session = Depends(get_db)):
    existente = db.query(modelos.Servicio).filter(modelos.Servicio.nombre == nombre).first()
    if existente:
        raise HTTPException(status_code=400, detail="El servicio ya existe.")
    nuevo = modelos.Servicio(nombre=nombre, precio=precio)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Servicio creado exitosamente", "servicio": nuevo}

# Actualizar un servicio existente
@router.put("/{servicio_id}")
def actualizar_servicio(servicio_id: int, nombre: str = None, precio: float = None, db: Session = Depends(get_db)):
    servicio = db.query(modelos.Servicio).filter(modelos.Servicio.id == servicio_id).first()
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado.")
    if nombre:
        servicio.nombre = nombre
    if precio is not None:
        servicio.precio = precio
    db.commit()
    db.refresh(servicio)
    return {"mensaje": "Servicio actualizado correctamente", "servicio": servicio}

# Eliminar un servicio
@router.delete("/{servicio_id}")
def eliminar_servicio(servicio_id: int, db: Session = Depends(get_db)):
    servicio = db.query(modelos.Servicio).filter(modelos.Servicio.id == servicio_id).first()
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado.")
    db.delete(servicio)
    db.commit()
    return {"mensaje": "Servicio eliminado correctamente"}
