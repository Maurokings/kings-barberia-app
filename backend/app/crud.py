
from sqlalchemy.orm import Session
from app import modelos

# ------------------ USUARIOS ------------------

def get_usuario(db: Session, nombre_usuario: str):
    return db.query(modelos.Usuario).filter(modelos.Usuario.nombre_usuario == nombre_usuario).first()


# ------------------ BARBEROS ------------------

def get_barberos(db: Session):
    return db.query(modelos.Barbero).all()

def create_barbero(db: Session, nombre: str):
    nuevo = modelos.Barbero(nombre=nombre)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


# ------------------ SERVICIOS ------------------

def get_servicios(db: Session):
    return db.query(modelos.Servicio).all()

def create_servicio(db: Session, nombre: str, precio: float):
    nuevo = modelos.Servicio(nombre=nombre, precio=precio)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


# ------------------ CORTES ------------------

def get_cortes(db: Session):
    return db.query(modelos.Corte).all()

def create_corte(db: Session, barbero_id: int, servicio_id: int, cliente: str, precio: float, fecha: str):
    nuevo = modelos.Corte(
        barbero_id=barbero_id,
        servicio_id=servicio_id,
        cliente=cliente,
        precio=precio,
        fecha=fecha
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


# ------------------ GASTOS ------------------

def get_gastos(db: Session):
    return db.query(modelos.Gasto).all()

def create_gasto(db: Session, descripcion: str, monto: float, fecha: str):
    nuevo = modelos.Gasto(descripcion=descripcion, monto=monto, fecha=fecha)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
