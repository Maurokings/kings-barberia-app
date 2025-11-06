from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.modelos import Servicio

router = APIRouter(prefix="/servicios", tags=["Servicios"])

# Dependencia para obtener la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Crear nuevo servicio
@router.post("/")
def crear_servicio(nombre: str, precio: float, db: Session = Depends(get_db)):
    existente = db.query(Servicio).filter(Servicio.nombre == nombre).first()
    if existente:
        raise HTTPException(status_code=400, detail=f"El servicio '{nombre}' ya existe.")
    
    nuevo = Servicio(nombre=nombre, precio=precio)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {
        "mensaje": f"✅ Servicio '{nombre}' creado exitosamente.",
        "id": nuevo.id,
        "precio": nuevo.precio
    }

# ✅ Listar servicios
@router.get("/")
def listar_servicios(db: Session = Depends(get_db)):
    servicios = db.query(Servicio).all()
    return servicios

# ✅ Actualizar servicio
@router.put("/{servicio_id}")
def actualizar_servicio(servicio_id: int, nombre: str = None, precio: float = None, db: Session = Depends(get_db)):
    servicio = db.query(Servicio).filter(Servicio.id == servicio_id).first()
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado.")

    if nombre:
        servicio.nombre = nombre
    if precio is not None:
        servicio.precio = precio

    db.commit()
    db.refresh(servicio)
    return {
        "mensaje": f"✅ Servicio '{servicio.nombre}' actualizado correctamente.",
        "id": servicio.id,
        "precio": servicio.precio
    }

# ✅ Eliminar servicio
@router.delete("/{servicio_id}")
def eliminar_servicio(servicio_id: int, db: Session = Depends(get_db)):
    servicio = db.query(Servicio).filter(Servicio.id == servicio_id).first()
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado.")
    db.delete(servicio)
    db.commit()
    return {"mensaje": f"Servicio '{servicio.nombre}' eliminado correctamente."}
