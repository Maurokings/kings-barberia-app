
from .modelos import Usuario, Barbero, Servicio, Corte, Gasto
from sqlmodel import Session, select
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_default_data(engine):
    with Session(engine) as session:
        # check if admin exists
        res = session.exec(select(Usuario).where(Usuario.username == "KingsBarberia")).first()
        if not res:
            admin = Usuario(username="KingsBarberia", password_hash=get_password_hash("Riverplate22"), nombre="Administrador", rol="admin")
            session.add(admin)
        # barberos
        for name in ["Gustavo","Mauro","Alejandro"]:
            exist = session.exec(select(Barbero).where(Barbero.nombre == name)).first()
            if not exist:
                b = Barbero(nombre=name, porcentaje=50.0)
                session.add(b)
        # servicios
        services = [("Corte", 10000), ("Corte + Barba", 12000), ("Claritos", 2500), ("Global", 15000)]
        for sname, price in services:
            ex = session.exec(select(Servicio).where(Servicio.nombre == sname)).first()
            if not ex:
                session.add(Servicio(nombre=sname, precio_sugerido=price))
        session.commit()
