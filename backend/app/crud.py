
from sqlalchemy.orm import Session
from app import modelos
from datetime import datetime

# ---------------------------------
# USUARIOS
# ---------------------------------
def obtener_usuario_por_nombre(db: Session, nombre_usuario: str):
    return db.query(modelos.Usuario).filter(modelos.Usuario.nombre_usuario == nombre_usuario).first()


# ---------------------------------
# BARBEROS
# ---------------------------------
def obtener_barberos(db: Session):
    return db.query(modelos.Barbero).all()

def crear_barbero(db: Session, nombre: str, porcentaje: float, contraseña: str):
    nuevo_barbero = modelos.Barbero(nombre=nombre, porcentaje=porcentaje, contraseña=contraseña)
    db.add(nuevo_barbero)
    db.commit()
    db.refresh(nuevo_barbero)
    return nuevo_barbero

def eliminar_barbero(db: Session, barbero_id: int):
    barbero = db.query(modelos.Barbero).filter(modelos.Barbero.id == barbero_id).first()
    if barbero:
        db.delete(barbero)
        db.commit()
    return barbero


# ---------------------------------
# SERVICIOS
# ---------------------------------
def obtener_servicios(db: Session):
    return db.query(modelos.Servicio).all()

def crear_servicio(db: Session, nombre: str, precio: float):
    nuevo_servicio = modelos.Servicio(nombre=nombre, precio=precio)
    db.add(nuevo_servicio)
    db.commit()
    db.refresh(nuevo_servicio)
    return nuevo_servicio


# ---------------------------------
# CORTES
# ---------------------------------
def registrar_corte(db: Session, barbero_id: int, servicio_id: int, metodo_pago: str, monto: float):
    nuevo_corte = modelos.Corte(
        barbero_id=barbero_id,
        servicio_id=servicio_id,
        metodo_pago=metodo_pago,
        monto=monto,
        fecha=datetime.utcnow()
    )
    db.add(nuevo_corte)
    db.commit()
    db.refresh(nuevo_corte)
    return nuevo_corte

def obtener_cortes(db: Session):
    return db.query(modelos.Corte).order_by(modelos.Corte.fecha.desc()).all()


# ---------------------------------
# GASTOS
# ---------------------------------
def registrar_gasto(db: Session, descripcion: str, monto: float):
    nuevo_gasto = modelos.Gasto(descripcion=descripcion, monto=monto, fecha=datetime.utcnow())
    db.add(nuevo_gasto)
    db.commit()
    db.refresh(nuevo_gasto)
    return nuevo_gasto

def obtener_gastos(db: Session):
    return db.query(modelos.Gasto).order_by(modelos.Gasto.fecha.desc()).all()
