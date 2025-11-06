from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import modelos
from app.database import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/barberos", tags=["Barberos"])

class BarberoBase(BaseModel):
    nombre: str
    porcentaje: float

class BarberoCreate(BarberoBase):
    contraseña: str

class BarberoResponse(BarberoBase):
    id: int

    class Config:
        orm_mode = True


@router.get("/", response_model=list[BarberoResponse])
def obtener_barberos(db: Session = Depends(get_db)):
    return db.query(modelos.Barbero).all()


@router.post("/", response_model=BarberoResponse)
def crear_barbero(barbero: BarberoCreate, db: Session = Depends(get_db)):
    nuevo_barbero = modelos.Barbero(
        nombre=barbero.nombre,
        porcentaje=barbero.porcentaje,
        contraseña=barbero.contraseña
    )
    db.add(nuevo_barbero)
    db.commit()
    db.refresh(nuevo_barbero)
    return nuevo_barbero


@router.put("/{barbero_id}", response_model=BarberoResponse)
def actualizar_barbero(barbero_id: int, barbero: BarberoBase, db: Session = Depends(get_db)):
    db_barbero = db.query(modelos.Barbero).filter(modelos.Barbero.id == barbero_id).first()
    if not db_barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado")
    db_barbero.nombre = barbero.nombre
    db_barbero.porcentaje = barbero.porcentaje
    db.commit()
    db.refresh(db_barbero)
    return db_barbero


@router.delete("/{barbero_id}")
def eliminar_barbero(barbero_id: int, db: Session = Depends(get_db)):
    db_barbero = db.query(modelos.Barbero).filter(modelos.Barbero.id == barbero_id).first()
    if not db_barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado")
    db.delete(db_barbero)
    db.commit()
    return {"mensaje": "Barbero eliminado exitosamente"}

