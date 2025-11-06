from app.database import SessionLocal, Base, engine
from app.modelos import Usuario

def crear_admin():
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    existente = db.query(Usuario).filter(Usuario.nombre_usuario == "KingsBarberia").first()
    if existente:
        print("⚠️ El usuario KingsBarberia ya existe.")
        return
    admin = Usuario(nombre_usuario="KingsBarberia", contraseña="Riverplate22", rol="admin")
    db.add(admin)
    db.commit()
    db.refresh(admin)
    db.close()
    print("✅ Usuario KingsBarberia creado exitosamente.")

if __name__ == "__main__":
    crear_admin()
