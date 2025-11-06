
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import modelos

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)

@router.post("/login")
def login(nombre_usuario: str, contraseña: str, db: Session = Depends(get_db)):
    usuario = db.query(modelos.Usuario).filter(modelos.Usuario.nombre_usuario == nombre_usuario).first()
    if not usuario or usuario.contraseña != contraseña:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"mensaje": "Inicio de sesión exitoso", "usuario": usuario.nombre_usuario, "rol": usuario.rol}

