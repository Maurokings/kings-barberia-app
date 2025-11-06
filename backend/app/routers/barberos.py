from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.modelos import Barbero

router = APIRouter(prefix="/barberos", tags=["Barberos"])

# Dependencia para obtener la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Crear nuevo barbero
@router.post("/")
def crear_barbero(nombre: str, contraseña: str, porcentaje: float = 50.0, db: Session = Depends(get_db)):
    existente = db.query(Barbero).filter(Barbero.nombre == nombre).first()
    if existente:
        raise HTTPException(status_code=400, detail=f"El barbero '{nombre}' ya existe.")
    
    nuevo = Barbero(nombre=nombre, contraseña=contraseña, porcentaje=porcentaje)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {
        "mensaje": f"✅ Barbero '{nombre}' creado exitosamente.",
        "id": nuevo.id,
        "porcentaje": nuevo.porcentaje
    }

# ✅ Obtener lista de barberos
@router.get("/")
def listar_barberos(db: Session = Depends(get_db)):
    barberos = db.query(Barbero).all()
    return barberos

# ✅ Eliminar un barbero (opcional)
@router.delete("/{barbero_id}")
def eliminar_barbero(barbero_id: int, db: Session = Depends(get_db)):
    barbero = db.query(Barbero).filter(Barbero.id == barbero_id).first()
    if not barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado.")
    db.delete(barbero)
    db.commit()
    return {"mensaje": f"Barbero '{barbero.nombre}' eliminado correctamente."}

